#!/bin/bash
set -e
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
WHITE='\033[1;37m'
GRAY='\033[0;90m'
BOLD='\033[1m'
NC='\033[0m'

print_banner() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                                                                              ║${NC}"
    echo -e "${CYAN}║   ${WHITE}${BOLD}MULTI-TOOL PROFESSIONAL SUITE${CYAN}                                             ║${NC}"
    echo -e "${CYAN}║   ${GREEN}Installer & Launcher v3.0.0${CYAN}                                                ║${NC}"
    echo -e "${CYAN}║   ${GRAY}System Update | Dependency Install | Auto-Launch${CYAN}                          ║${NC}"
    echo -e "${CYAN}║                                                                              ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_line() {
    echo -e "${CYAN}════════════════════════════════════════════════════════════════════════════════${NC}"
}

print_success() { echo -e "${GREEN}[OK]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }
print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARN]${NC} $1"; }
print_step() {
    echo -e "\n${MAGENTA}${BOLD}▶ $1${NC}"
    print_line
}

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then OS="debian"
        elif [ -f /etc/redhat-release ]; then OS="redhat"
        elif [ -f /etc/arch-release ]; then OS="arch"
        else OS="linux"; fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then OS="macos"
    else OS="unknown"; fi
    print_info "Detected OS: $OS"
}

update_system() {
    print_step "Updating System Packages"
    case $OS in
        debian)
            print_info "Updating APT..."
            sudo apt-get update -qq && sudo apt-get upgrade -y -qq
            print_success "System updated"
            ;;
        redhat)
            print_info "Updating YUM..."
            sudo yum update -y -q
            print_success "System updated"
            ;;
        arch)
            print_info "Updating Arch..."
            sudo pacman -Syu --noconfirm -q
            print_success "System updated"
            ;;
        macos)
            if command -v brew &> /dev/null; then
                brew update -q && brew upgrade -q
                print_success "System updated"
            else
                print_warning "Homebrew not found. Skipping."
            fi
            ;;
        *) print_warning "Unknown OS. Skipping update." ;;
    esac
}

check_python() {
    print_step "Checking Python"
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION found"
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION found"
        PYTHON_CMD="python"
    else
        print_warning "Python not found. Installing..."
        case $OS in
            debian) sudo apt-get install -y -qq python3 python3-pip ;;
            redhat) sudo yum install -y -q python3 python3-pip ;;
            arch) sudo pacman -S --noconfirm -q python python-pip ;;
            macos)
                if command -v brew &> /dev/null; then
                    brew install python@3.11
                else
                    print_error "Install Python manually from python.org"
                    exit 1
                fi
                ;;
        esac
        PYTHON_CMD="python3"
        print_success "Python installed"
    fi
}

install_pip_packages() {
    print_step "Installing Python Packages"
    PACKAGES="requests urllib3 Pillow qrcode pyjwt cryptography colorama psutil speedtest-cli whois dnspython pyfiglet termcolor"
    for pkg in $PACKAGES; do
        print_info "Installing $pkg..."
        $PYTHON_CMD -m pip install --upgrade --quiet "$pkg" 2>/dev/null || print_warning "Failed: $pkg (optional)"
    done
    print_success "Packages installed"
}

install_system_packages() {
    print_step "Installing System Packages"
    case $OS in
        debian)
            sudo apt-get install -y -qq curl wget git build-essential libssl-dev zlib1g-dev \
                libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev \
                libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl 2>/dev/null || true
            ;;
        redhat)
            sudo yum install -y -q curl wget git gcc openssl-devel bzip2-devel libffi-devel zlib-devel 2>/dev/null || true
            ;;
        arch)
            sudo pacman -S --noconfirm -q curl wget git base-devel openssl zlib 2>/dev/null || true
            ;;
        macos)
            brew install curl wget git openssl readline sqlite3 xz zlib 2>/dev/null || true
            ;;
    esac
    print_success "System packages installed"
}

setup_script() {
    print_step "Setting Up Script"
    SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/w.py"
    if [ ! -f "$SCRIPT_PATH" ]; then
        print_error "w.py not found in current directory"
        exit 1
    fi
    chmod +x "$SCRIPT_PATH"
    print_success "Script ready"
}

launch_app() {
    print_step "Launching Multi-Tool Suite"
    SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/w.py"
    print_info "Starting..."
    sleep 1
    clear
    exec $PYTHON_CMD "$SCRIPT_PATH"
}

main() {
    clear
    print_banner
    print_info "Starting installation..."
    detect_os
    update_system
    install_system_packages
    check_python
    install_pip_packages
    setup_script
    print_line
    print_success "Installation complete!"
    print_line
    sleep 2
    launch_app
}

trap 'echo -e "\n${RED}Interrupted${NC}"; exit 1' INT TERM
main
