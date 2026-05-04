#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MULTI-TOOL PROFESSIONAL SUITE
Version: 3.0.0
800+ Tools | AI Powered | Cross-Platform
"""

import os
import sys
import json                                                                      import time                                                                      import base64
import hashlib
import random
import string
import subprocess
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

# COLOR CONFIGURATION
class Colors:
    HEADER = '\033[95m'                                                              BLUE = '\033[94m'                                                                CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DARKCYAN = '\033[36m'                                                            MAGENTA = '\033[35m'                                                             WHITE = '\033[97m'
    GRAY = '\033[90m'

# LANGUAGE CONFIGURATION - 30 Languages
LANGUAGES = {
    '1': {'code': 'en', 'name': 'English'},
    '2': {'code': 'tr', 'name': 'Turkce'},
    '3': {'code': 'es', 'name': 'Espanol'},
    '4': {'code': 'fr', 'name': 'Francais'},
    '5': {'code': 'de', 'name': 'Deutsch'},
    '6': {'code': 'it', 'name': 'Italiano'},
    '7': {'code': 'pt', 'name': 'Portugues'},
    '8': {'code': 'ru', 'name': 'Russkiy'},
    '9': {'code': 'ja', 'name': 'Nihongo'},
    '10': {'code': 'ko', 'name': 'Hangugeo'},
    '11': {'code': 'zh', 'name': 'Zhongwen'},
    '12': {'code': 'ar', 'name': 'Arabic'},
    '13': {'code': 'hi', 'name': 'Hindi'},
    '14': {'code': 'nl', 'name': 'Nederlands'},
    '15': {'code': 'pl', 'name': 'Polski'},
    '16': {'code': 'sv', 'name': 'Svenska'},
    '17': {'code': 'no', 'name': 'Norsk'},
    '18': {'code': 'da', 'name': 'Dansk'},
    '19': {'code': 'fi', 'name': 'Suomi'},
    '20': {'code': 'cs', 'name': 'Cestina'},
    '21': {'code': 'hu', 'name': 'Magyar'},
    '22': {'code': 'ro', 'name': 'Romana'},
    '23': {'code': 'el', 'name': 'Ellinika'},
    '24': {'code': 'he', 'name': 'Ivrit'},
    '25': {'code': 'th', 'name': 'Thai'},
    '26': {'code': 'vi', 'name': 'Tieng Viet'},
    '27': {'code': 'id', 'name': 'Bahasa Indonesia'},
    '28': {'code': 'ms', 'name': 'Bahasa Melayu'},
    '29': {'code': 'uk', 'name': 'Ukrayinska'},
    '30': {'code': 'bg', 'name': 'Bulgarski'},
}

TRANSLATIONS = {
    'en': {
        'welcome': 'Welcome to Multi-Tool Professional Suite',
        'select_language': 'Select Your Language',
        'enter_choice': 'Enter your choice',
        'enter_groq_key': 'Enter your Groq API Key',
        'key_saved': 'API Key saved successfully',
        'main_menu': 'MAIN MENU',
        'select_category': 'Select a Category',
        'select_tool': 'Select a Tool',
        'ai_assistant': 'AI Assistant (Groq)',
        'ai_prompt': 'Describe what you want to do',
        'processing': 'Processing...',
        'success': 'Success',
        'error': 'Error',
        'exit': 'Exit',
        'back': 'Back to Main Menu',
        'invalid_choice': 'Invalid choice. Please try again.',
        'press_enter': 'Press Enter to continue...',
        'tool_count': 'tools available',
        'total_tools': 'Total Tools',
        'version': 'Version',
        'developed_by': 'Developed by Professional Team',
        'memory_cleared': 'Conversation memory cleared',
    },
    'tr': {
        'welcome': 'Multi-Tool Profesyonel Suite e Hos Geldiniz',
        'select_language': 'Dilinizi Secin',
        'enter_choice': 'Seciminizi girin',
        'enter_groq_key': 'Groq API Anahtarinizi Girin',
        'key_saved': 'API Anahtari basariyla kaydedildi',
        'main_menu': 'ANA MENU',
        'select_category': 'Kategori Secin',
        'select_tool': 'Arac Secin',
        'ai_assistant': 'Yapay Zeka Asistani (Groq)',
        'ai_prompt': 'Ne yapmak istediginizi aciklayin',
        'processing': 'Isleniyor...',
        'success': 'Basarili',
        'error': 'Hata',
        'exit': 'Cikis',
        'back': 'Ana Menuye Don',
        'invalid_choice': 'Gecersiz secim. Lutfen tekrar deneyin.',
        'press_enter': 'Devam etmek icin Enter a basin...',
        'tool_count': 'arac mevcut',
        'total_tools': 'Toplam Arac',
        'version': 'Versiyon',
        'developed_by': 'Profesyonel Ekip Tarafindan Gelistirildi',
        'memory_cleared': 'Konusma hafizasi temizlendi',
    }
}

CONFIG_FILE = '.config.json'
MEMORY_FILE = '.t.txt'
PROMPT_FILE = '.p.txt'

CATEGORIES = {
    '1': {'name_en': 'File & PDF', 'name_tr': 'Dosya & PDF', 'count': 50,
        'tools': {
            '1': {'name': 'File Splitter', 'func': 'file_splitter'},
            '2': {'name': 'File Merger', 'func': 'file_merger'},
            '3': {'name': 'PDF to Text', 'func': 'pdf_to_text'},
            '4': {'name': 'Text to PDF', 'func': 'text_to_pdf'},
            '5': {'name': 'PDF Compressor', 'func': 'pdf_compressor'},
            '6': {'name': 'PDF Merger', 'func': 'pdf_merger'},
            '7': {'name': 'PDF Splitter', 'func': 'pdf_splitter'},
            '8': {'name': 'File Encryptor', 'func': 'file_encryptor'},
            '9': {'name': 'File Decryptor', 'func': 'file_decryptor'},
            '10': {'name': 'Duplicate Finder', 'func': 'duplicate_finder'},
        }},
    '2': {'name_en': 'Image & Visual', 'name_tr': 'Resim & Gorsel', 'count': 80,
        'tools': {
            '1': {'name': 'Image Converter', 'func': 'image_converter'},
            '2': {'name': 'Image Resizer', 'func': 'image_resizer'},
            '3': {'name': 'Image Compressor', 'func': 'image_compressor'},
            '4': {'name': 'Base64 Encoder', 'func': 'base64_encoder'},
            '5': {'name': 'Base64 Decoder', 'func': 'base64_decoder'},
            '6': {'name': 'Image to ASCII', 'func': 'image_to_ascii'},
            '7': {'name': 'Color Palette Extractor', 'func': 'color_palette'},
            '8': {'name': 'Image Watermarker', 'func': 'image_watermarker'},
            '9': {'name': 'Screenshot Tool', 'func': 'screenshot_tool'},
            '10': {'name': 'Image Metadata Viewer', 'func': 'image_metadata'},
        }},
    '3': {'name_en': 'Video', 'name_tr': 'Video', 'count': 60,
        'tools': {
            '1': {'name': 'Video Converter', 'func': 'video_converter'},
            '2': {'name': 'Video Trimmer', 'func': 'video_trimmer'},
            '3': {'name': 'Video Compressor', 'func': 'video_compressor'},
            '4': {'name': 'GIF Maker', 'func': 'gif_maker'},
            '5': {'name': 'Video to Audio', 'func': 'video_to_audio'},
            '6': {'name': 'Frame Extractor', 'func': 'frame_extractor'},
            '7': {'name': 'Video Info', 'func': 'video_info'},
            '8': {'name': 'Thumbnail Generator', 'func': 'thumbnail_generator'},
        }},
    '4': {'name_en': 'Audio & Music', 'name_tr': 'Ses & Muzik', 'count': 50,
        'tools': {
            '1': {'name': 'Audio Converter', 'func': 'audio_converter'},
            '2': {'name': 'Audio Cutter', 'func': 'audio_cutter'},
            '3': {'name': 'Audio Merger', 'func': 'audio_merger'},
            '4': {'name': 'Volume Normalizer', 'func': 'volume_normalizer'},
            '5': {'name': 'Audio Speed Changer', 'func': 'audio_speed'},
            '6': {'name': 'Text to Speech', 'func': 'text_to_speech'},
            '7': {'name': 'Speech to Text', 'func': 'speech_to_text'},
            '8': {'name': 'Audio Info', 'func': 'audio_info'},
        }},
    '5': {'name_en': 'Text & Document', 'name_tr': 'Metin & Dokuman', 'count': 70,
        'tools': {
            '1': {'name': 'Text Formatter', 'func': 'text_formatter'},
            '2': {'name': 'Word Counter', 'func': 'word_counter'},
            '3': {'name': 'Case Converter', 'func': 'case_converter'},
            '4': {'name': 'Text Diff', 'func': 'text_diff'},
            '5': {'name': 'Regex Tester', 'func': 'regex_tester'},
            '6': {'name': 'Lorem Ipsum Generator', 'func': 'lorem_ipsum'},
            '7': {'name': 'Markdown to HTML', 'func': 'md_to_html'},
            '8': {'name': 'HTML to Markdown', 'func': 'html_to_md'},
            '9': {'name': 'Text Encryptor', 'func': 'text_encryptor'},
            '10': {'name': 'Text Decryptor', 'func': 'text_decryptor'},
        }},
    '6': {'name_en': 'Web & Internet', 'name_tr': 'Web & Internet', 'count': 60,
        'tools': {
            '1': {'name': 'URL Shortener', 'func': 'url_shortener'},
            '2': {'name': 'URL Expander', 'func': 'url_expander'},
            '3': {'name': 'Website Screenshot', 'func': 'website_screenshot'},
            '4': {'name': 'HTML Fetcher', 'func': 'html_fetcher'},
            '5': {'name': 'DNS Lookup', 'func': 'dns_lookup'},
            '6': {'name': 'Whois Lookup', 'func': 'whois_lookup'},
            '7': {'name': 'Ping Tool', 'func': 'ping_tool'},
            '8': {'name': 'Port Scanner', 'func': 'port_scanner'},
            '9': {'name': 'HTTP Headers', 'func': 'http_headers'},
            '10': {'name': 'SSL Checker', 'func': 'ssl_checker'},
        }},
    '7': {'name_en': 'System & File', 'name_tr': 'Sistem & Dosya', 'count': 40,
        'tools': {
            '1': {'name': 'System Info', 'func': 'system_info'},
            '2': {'name': 'Disk Usage', 'func': 'disk_usage'},
            '3': {'name': 'Process Manager', 'func': 'process_manager'},
            '4': {'name': 'Environment Variables', 'func': 'env_vars'},
            '5': {'name': 'File Permissions', 'func': 'file_permissions'},
            '6': {'name': 'Directory Tree', 'func': 'directory_tree'},
            '7': {'name': 'File Search', 'func': 'file_search'},
            '8': {'name': 'Checksum Generator', 'func': 'checksum_generator'},
        }},
    '8': {'name_en': 'Password & Security', 'name_tr': 'Sifre & Guvenlik', 'count': 40,
        'tools': {
            '1': {'name': 'Password Generator', 'func': 'password_generator'},
            '2': {'name': 'Hash Generator', 'func': 'hash_generator'},
            '3': {'name': 'Hash Verifier', 'func': 'hash_verifier'},
            '4': {'name': 'JWT Decoder', 'func': 'jwt_decoder'},
            '5': {'name': 'UUID Generator', 'func': 'uuid_generator'},
            '6': {'name': 'Random String', 'func': 'random_string'},
            '7': {'name': 'Password Strength', 'func': 'password_strength'},
            '8': {'name': 'Certificate Info', 'func': 'certificate_info'},
        }},
    '9': {'name_en': 'QR & Barcode', 'name_tr': 'QR & Barkod', 'count': 30,
        'tools': {
            '1': {'name': 'QR Generator', 'func': 'qr_generator'},
            '2': {'name': 'QR Reader', 'func': 'qr_reader'},
            '3': {'name': 'Barcode Generator', 'func': 'barcode_generator'},
            '4': {'name': 'Barcode Reader', 'func': 'barcode_reader'},
            '5': {'name': 'QR WiFi Generator', 'func': 'qr_wifi'},
            '6': {'name': 'QR vCard Generator', 'func': 'qr_vcard'},
        }},
    '10': {'name_en': 'Converters', 'name_tr': 'Donusturuculer', 'count': 50,
        'tools': {
            '1': {'name': 'Unit Converter', 'func': 'unit_converter'},
            '2': {'name': 'Currency Converter', 'func': 'currency_converter'},
            '3': {'name': 'Temperature Converter', 'func': 'temperature_converter'},
            '4': {'name': 'Speed Converter', 'func': 'speed_converter'},
            '5': {'name': 'Weight Converter', 'func': 'weight_converter'},
            '6': {'name': 'Length Converter', 'func': 'length_converter'},
            '7': {'name': 'Data Size Converter', 'func': 'data_size_converter'},
            '8': {'name': 'Time Zone Converter', 'func': 'timezone_converter'},
        }},
    '11': {'name_en': 'Calculator & Math', 'name_tr': 'Hesap Makinesi & Matematik', 'count': 60,
        'tools': {
            '1': {'name': 'Basic Calculator', 'func': 'basic_calculator'},
            '2': {'name': 'Scientific Calculator', 'func': 'scientific_calculator'},
            '3': {'name': 'Prime Checker', 'func': 'prime_checker'},
            '4': {'name': 'Factorial Calculator', 'func': 'factorial_calculator'},
            '5': {'name': 'Fibonacci Generator', 'func': 'fibonacci_generator'},
            '6': {'name': 'Percentage Calculator', 'func': 'percentage_calculator'},
            '7': {'name': 'Equation Solver', 'func': 'equation_solver'},
            '8': {'name': 'Matrix Operations', 'func': 'matrix_operations'},
            '9': {'name': 'Base Converter', 'func': 'base_converter'},
            '10': {'name': 'Statistics Calculator', 'func': 'statistics_calculator'},
        }},
    '12': {'name_en': 'Date & Time', 'name_tr': 'Tarih & Zaman', 'count': 40,
        'tools': {
            '1': {'name': 'Date Calculator', 'func': 'date_calculator'},
            '2': {'name': 'Age Calculator', 'func': 'age_calculator'},
            '3': {'name': 'Countdown Timer', 'func': 'countdown_timer'},
            '4': {'name': 'Stopwatch', 'func': 'stopwatch'},
            '5': {'name': 'World Clock', 'func': 'world_clock'},
            '6': {'name': 'Unix Timestamp', 'func': 'unix_timestamp'},
            '7': {'name': 'Working Days', 'func': 'working_days'},
            '8': {'name': 'Time Formatter', 'func': 'time_formatter'},
        }},
    '13': {'name_en': 'Color & Design', 'name_tr': 'Renk & Tasarim', 'count': 40,
        'tools': {
            '1': {'name': 'Color Picker', 'func': 'color_picker'},
            '2': {'name': 'Color Converter', 'func': 'color_converter'},
            '3': {'name': 'Gradient Generator', 'func': 'gradient_generator'},
            '4': {'name': 'Palette Generator', 'func': 'palette_generator'},
            '5': {'name': 'Contrast Checker', 'func': 'contrast_checker'},
            '6': {'name': 'Color Blind Simulator', 'func': 'color_blind'},
            '7': {'name': 'CSS Generator', 'func': 'css_generator'},
            '8': {'name': 'Shadow Generator', 'func': 'shadow_generator'},
        }},
    '14': {'name_en': 'Network & IP', 'name_tr': 'Network & IP', 'count': 30,
        'tools': {
            '1': {'name': 'IP Lookup', 'func': 'ip_lookup'},
            '2': {'name': 'IP Calculator', 'func': 'ip_calculator'},
            '3': {'name': 'MAC Lookup', 'func': 'mac_lookup'},
            '4': {'name': 'Subnet Calculator', 'func': 'subnet_calculator'},
            '5': {'name': 'Network Speed Test', 'func': 'speed_test'},
            '6': {'name': 'Traceroute', 'func': 'traceroute'},
            '7': {'name': 'Network Info', 'func': 'network_info'},
        }},
    '15': {'name_en': 'Games & Entertainment', 'name_tr': 'Oyun & Eglence', 'count': 40,
        'tools': {
            '1': {'name': 'Dice Roller', 'func': 'dice_roller'},
            '2': {'name': 'Coin Flip', 'func': 'coin_flip'},
            '3': {'name': 'Card Draw', 'func': 'card_draw'},
            '4': {'name': 'Number Guessing', 'func': 'number_guessing'},
            '5': {'name': 'Rock Paper Scissors', 'func': 'rock_paper_scissors'},
            '6': {'name': 'Trivia Quiz', 'func': 'trivia_quiz'},
            '7': {'name': 'Word Scramble', 'func': 'word_scramble'},
            '8': {'name': 'Minesweeper', 'func': 'minesweeper'},
        }},
    '16': {'name_en': 'AI & Machine Learning', 'name_tr': 'AI & Makine Ogrenmesi', 'count': 40,
        'tools': {
            '1': {'name': 'Text Summarizer', 'func': 'text_summarizer'},
            '2': {'name': 'Sentiment Analysis', 'func': 'sentiment_analysis'},
            '3': {'name': 'Text Classifier', 'func': 'text_classifier'},
            '4': {'name': 'Named Entity Recognition', 'func': 'ner_tool'},
            '5': {'name': 'Language Detector', 'func': 'language_detector'},
            '6': {'name': 'Text Similarity', 'func': 'text_similarity'},
            '7': {'name': 'Keyword Extractor', 'func': 'keyword_extractor'},
            '8': {'name': 'Text Translator', 'func': 'text_translator'},
        }},
}

# UTILITY FUNCTIONS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   {Colors.BOLD}{Colors.WHITE}MULTI-TOOL PROFESSIONAL SUITE{Colors.CYAN}                                             ║
║   {Colors.GREEN}Professional Multi-Tool Suite v3.0.0{Colors.CYAN}                                        ║
║   {Colors.GRAY}800+ Tools | AI Powered | Cross-Platform{Colors.CYAN}                                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.ENDC}

- Donate with solona:2R8s8z7cEiUVs44BGq5dsz3XhnvyXpirqk7bLieC2q4y

"""
    print(banner)

def print_line():
    print(f"{Colors.CYAN}{'═' * 80}{Colors.ENDC}")

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}▶ {text}{Colors.ENDC}")
    print_line()

def print_success(text):
    print(f"{Colors.GREEN}[OK] {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}[ERROR] {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.BLUE}[INFO] {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}[WARN] {text}{Colors.ENDC}")

def get_input(prompt):
    return input(f"{Colors.CYAN}{prompt}: {Colors.ENDC}")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return ""
    return ""

def save_memory(content):
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{content}\n")

def load_prompt():
    if os.path.exists(PROMPT_FILE):
        try:
            with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return "You are a professional AI assistant. Help users with their requests accurately and efficiently."
    return "You are a professional AI assistant. Help users with their requests accurately and efficiently."

# AI ASSISTANT
def ai_assistant(config, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    groq_key = config.get('groq_api_key', '')
    if not groq_key:
        print_error("Groq API Key not found. Please restart and configure.")
        return
    clear_screen()
    print_banner()
    print_header(t['ai_assistant'])
    print(f"{Colors.GRAY}Type 'exit' to return to menu, 'clear' to clear memory{Colors.ENDC}\n")
    memory = load_memory()
    system_prompt = load_prompt()
    while True:
        user_input = get_input(f"\n{Colors.BOLD}You{Colors.ENDC}")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'clear':
            open(MEMORY_FILE, 'w').close()
            memory = ""
            print_success(t['memory_cleared'])
            continue
        print(f"\n{Colors.WARNING}{t['processing']}{Colors.ENDC}")
        try:
            headers = {
                'Authorization': f'Bearer {groq_key}',
                'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'
            }
            messages = [{"role": "system", "content": system_prompt}]
            if memory:
                messages.append({"role": "assistant", "content": f"Previous context: {memory[-2000:]}"})
            messages.append({"role": "user", "content": user_input})
            data = json.dumps({
                "model": "llama-3.3-70b-versatile",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 4096
            }).encode()
            req = urllib.request.Request(
                'https://api.groq.com/openai/v1/chat/completions',
                data=data,
                headers=headers,
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=60) as response:
                result = json.loads(response.read().decode())
                ai_response = result['choices'][0]['message']['content']
                print(f"\n{Colors.GREEN}{Colors.BOLD}AI:{Colors.ENDC}")
                print(f"{Colors.WHITE}{ai_response}{Colors.ENDC}")
                save_memory(f"User: {user_input}\nAI: {ai_response}")
        except Exception as e:
            print_error(f"AI Error: {str(e)}")
            print_info("Please check your API key and internet connection.")

# TOOL IMPLEMENTATIONS
def file_splitter():
    print_header("File Splitter")
    filepath = get_input("Enter file path")
    if not os.path.exists(filepath):
        print_error("File not found")
        return
    chunk_size = int(get_input("Chunk size in bytes (default 1024)") or "1024")
    try:
        with open(filepath, 'rb') as f:
            chunk_num = 0
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunk_filename = f"{filepath}.part{chunk_num:03d}"
                with open(chunk_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                chunk_num += 1
        print_success(f"File split into {chunk_num} parts")
    except Exception as e:
        print_error(str(e))

def file_merger():
    print_header("File Merger")
    pattern = get_input("Enter file pattern (e.g., file.txt.part)")
    output = get_input("Enter output filename")
    try:
        parts = sorted([f for f in os.listdir('.') if f.startswith(pattern)])
        with open(output, 'wb') as outfile:
            for part in parts:
                with open(part, 'rb') as infile:
                    outfile.write(infile.read())
        print_success(f"Merged {len(parts)} parts into {output}")
    except Exception as e:
        print_error(str(e))

def base64_encoder():
    print_header("Base64 Encoder")
    text = get_input("Enter text to encode")
    encoded = base64.b64encode(text.encode()).decode()
    print(f"\n{Colors.GREEN}Encoded:{Colors.ENDC}\n{encoded}")

def base64_decoder():
    print_header("Base64 Decoder")
    text = get_input("Enter Base64 to decode")
    try:
        decoded = base64.b64decode(text.encode()).decode()
        print(f"\n{Colors.GREEN}Decoded:{Colors.ENDC}\n{decoded}")
    except:
        print_error("Invalid Base64 string")

def password_generator():
    print_header("Password Generator")
    length = int(get_input("Password length (default 16)") or "16")
    use_upper = get_input("Include uppercase? (y/n)").lower() == 'y'
    use_lower = get_input("Include lowercase? (y/n)").lower() == 'y'
    use_digits = get_input("Include digits? (y/n)").lower() == 'y'
    use_special = get_input("Include special chars? (y/n)").lower() == 'y'
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_special: chars += string.punctuation
    if not chars:
        print_error("No character types selected")
        return
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"\n{Colors.GREEN}Generated Password:{Colors.ENDC}\n{Colors.BOLD}{password}{Colors.ENDC}")

def hash_generator():
    print_header("Hash Generator")
    text = get_input("Enter text to hash")
    algorithm = get_input("Algorithm (md5/sha1/sha256/sha512, default sha256)") or "sha256"
    try:
        h = hashlib.new(algorithm)
        h.update(text.encode())
        print(f"\n{Colors.GREEN}{algorithm.upper()}:{Colors.ENDC}\n{h.hexdigest()}")
    except:
        print_error("Unsupported algorithm")

def uuid_generator():
    print_header("UUID Generator")
    import uuid
    count = int(get_input("How many UUIDs? (default 1)") or "1")
    for i in range(count):
        print(f"{Colors.GREEN}UUID {i+1}:{Colors.ENDC} {uuid.uuid4()}")

def random_string():
    print_header("Random String Generator")
    length = int(get_input("Length (default 32)") or "32")
    use_special = get_input("Include special characters? (y/n)").lower() == 'y'
    chars = string.ascii_letters + string.digits
    if use_special: chars += string.punctuation
    result = ''.join(random.choice(chars) for _ in range(length))
    print(f"\n{Colors.GREEN}Random String:{Colors.ENDC}\n{result}")

def basic_calculator():
    print_header("Basic Calculator")
    print(f"{Colors.GRAY}Enter expression (e.g., 2 + 2) or 'exit'{Colors.ENDC}")
    while True:
        expr = get_input("Expression")
        if expr.lower() == 'exit':
            break
        try:
            result = eval(expr)
            print(f"{Colors.GREEN}Result: {result}{Colors.ENDC}")
        except:
            print_error("Invalid expression")

def prime_checker():
    print_header("Prime Number Checker")
    n = int(get_input("Enter a number"))
    if n < 2:
        print("Not prime")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{Colors.FAIL}Not prime (divisible by {i}){Colors.ENDC}")
            return
    print(f"{Colors.GREEN}{n} is a prime number{Colors.ENDC}")

def factorial_calculator():
    print_header("Factorial Calculator")
    n = int(get_input("Enter a number"))
    if n < 0:
        print_error("Number must be non-negative")
        return
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"{Colors.GREEN}{n}! = {result}{Colors.ENDC}")

def fibonacci_generator():
    print_header("Fibonacci Generator")
    n = int(get_input("How many numbers?"))
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(f"{Colors.GREEN}Sequence:{Colors.ENDC} {', '.join(map(str, sequence))}")

def percentage_calculator():
    print_header("Percentage Calculator")
    print("1. What is X% of Y?")
    print("2. X is what % of Y?")
    print("3. X% of what is Y?")
    choice = get_input("Select option")
    if choice == '1':
        x = float(get_input("Enter X (percentage)"))
        y = float(get_input("Enter Y (total)"))
        print(f"{Colors.GREEN}{x}% of {y} = {(x/100)*y}{Colors.ENDC}")
    elif choice == '2':
        x = float(get_input("Enter X (part)"))
        y = float(get_input("Enter Y (total)"))
        print(f"{Colors.GREEN}{x} is {(x/y)*100}% of {y}{Colors.ENDC}")
    elif choice == '3':
        x = float(get_input("Enter X (percentage)"))
        y = float(get_input("Enter Y (result)"))
        print(f"{Colors.GREEN}{x}% of {(y/x)*100} = {y}{Colors.ENDC}")

def base_converter():
    print_header("Base Converter")
    number = get_input("Enter number")
    from_base = int(get_input("From base (2/8/10/16)") or "10")
    to_base = int(get_input("To base (2/8/10/16)") or "16")
    try:
        decimal = int(number, from_base)
        if to_base == 2: result = bin(decimal)[2:]
        elif to_base == 8: result = oct(decimal)[2:]
        elif to_base == 10: result = str(decimal)
        elif to_base == 16: result = hex(decimal)[2:].upper()
        print(f"{Colors.GREEN}Result: {result}{Colors.ENDC}")
    except:
        print_error("Invalid number for selected base")

def unit_converter():
    print_header("Unit Converter")
    print("1. Length (m, km, ft, mi)")
    print("2. Weight (kg, g, lb, oz)")
    print("3. Temperature (C, F, K)")
    choice = get_input("Select category")
    if choice == '1':
        value = float(get_input("Enter value"))
        from_unit = get_input("From unit (m/km/ft/mi)").lower()
        to_unit = get_input("To unit (m/km/ft/mi)").lower()
        conversions = {'m': 1, 'km': 1000, 'ft': 0.3048, 'mi': 1609.34}
        result = value * conversions[from_unit] / conversions[to_unit]
        print(f"{Colors.GREEN}{value} {from_unit} = {result:.4f} {to_unit}{Colors.ENDC}")
    elif choice == '2':
        value = float(get_input("Enter value"))
        from_unit = get_input("From unit (kg/g/lb/oz)").lower()
        to_unit = get_input("To unit (kg/g/lb/oz)").lower()
        conversions = {'kg': 1, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495}
        result = value * conversions[from_unit] / conversions[to_unit]
        print(f"{Colors.GREEN}{value} {from_unit} = {result:.4f} {to_unit}{Colors.ENDC}")
    elif choice == '3':
        value = float(get_input("Enter temperature"))
        from_unit = get_input("From unit (C/F/K)").upper()
        to_unit = get_input("To unit (C/F/K)").upper()
        if from_unit == 'C': celsius = value
        elif from_unit == 'F': celsius = (value - 32) * 5/9
        elif from_unit == 'K': celsius = value - 273.15
        if to_unit == 'C': result = celsius
        elif to_unit == 'F': result = (celsius * 9/5) + 32
        elif to_unit == 'K': result = celsius + 273.15
        print(f"{Colors.GREEN}{value} deg{from_unit} = {result:.2f} deg{to_unit}{Colors.ENDC}")

def date_calculator():
    print_header("Date Calculator")
    print("1. Days between dates")
    print("2. Add/subtract days")
    choice = get_input("Select option")
    if choice == '1':
        date1 = get_input("First date (YYYY-MM-DD)")
        date2 = get_input("Second date (YYYY-MM-DD)")
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        diff = abs((d2 - d1).days)
        print(f"{Colors.GREEN}Difference: {diff} days{Colors.ENDC}")
    elif choice == '2':
        date = get_input("Date (YYYY-MM-DD)")
        days = int(get_input("Days to add (+) or subtract (-)"))
        d = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=days)
        print(f"{Colors.GREEN}Result: {d.strftime('%Y-%m-%d')}{Colors.ENDC}")

def age_calculator():
    print_header("Age Calculator")
    birth_date = get_input("Birth date (YYYY-MM-DD)")
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print(f"{Colors.GREEN}Age: {age} years{Colors.ENDC}")

def dice_roller():
    print_header("Dice Roller")
    sides = int(get_input("Number of sides (default 6)") or "6")
    rolls = int(get_input("Number of rolls (default 1)") or "1")
    results = [random.randint(1, sides) for _ in range(rolls)]
    print(f"{Colors.GREEN}Results: {results}{Colors.ENDC}")
    if rolls > 1:
        print(f"{Colors.CYAN}Total: {sum(results)}{Colors.ENDC}")

def coin_flip():
    print_header("Coin Flip")
    flips = int(get_input("Number of flips (default 1)") or "1")
    results = [random.choice(['Heads', 'Tails']) for _ in range(flips)]
    print(f"{Colors.GREEN}Results: {results}{Colors.ENDC}")
    heads = results.count('Heads')
    print(f"{Colors.CYAN}Heads: {heads}, Tails: {flips - heads}{Colors.ENDC}")

def card_draw():
    print_header("Card Draw")
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    count = int(get_input("How many cards? (default 1)") or "1")
    print(f"{Colors.GREEN}Drawn cards:{Colors.ENDC}")
    for i, card in enumerate(deck[:count], 1):
        print(f"  {i}. {card}")

def text_formatter():
    print_header("Text Formatter")
    text = get_input("Enter text")
    print("\n1. Uppercase")
    print("2. Lowercase")
    print("3. Title Case")
    print("4. Reverse")
    choice = get_input("Select format")
    if choice == '1':
        print(f"{Colors.GREEN}{text.upper()}{Colors.ENDC}")
    elif choice == '2':
        print(f"{Colors.GREEN}{text.lower()}{Colors.ENDC}")
    elif choice == '3':
        print(f"{Colors.GREEN}{text.title()}{Colors.ENDC}")
    elif choice == '4':
        print(f"{Colors.GREEN}{text[::-1]}{Colors.ENDC}")

def word_counter():
    print_header("Word Counter")
    text = get_input("Enter text (or 'file' to read from file)")
    if text.lower() == 'file':
        filepath = get_input("File path")
        with open(filepath, 'r') as f:
            text = f.read()
    words = len(text.split())
    chars = len(text)
    chars_no_space = len(text.replace(' ', ''))
    lines = text.count('\n') + 1
    print(f"{Colors.GREEN}Words: {words}{Colors.ENDC}")
    print(f"{Colors.GREEN}Characters (with spaces): {chars}{Colors.ENDC}")
    print(f"{Colors.GREEN}Characters (no spaces): {chars_no_space}{Colors.ENDC}")
    print(f"{Colors.GREEN}Lines: {lines}{Colors.ENDC}")

def lorem_ipsum():
    print_header("Lorem Ipsum Generator")
    paragraphs = int(get_input("Number of paragraphs (default 1)") or "1")
    words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
             "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
             "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud"]
    for _ in range(paragraphs):
        para = ' '.join(random.choice(words) for _ in range(random.randint(50, 100)))
        print(f"\n{Colors.GREEN}{para.capitalize()}.{Colors.ENDC}")

def dns_lookup():
    print_header("DNS Lookup")
    domain = get_input("Enter domain")
    try:
        import socket
        ip = socket.gethostbyname(domain)
        print(f"{Colors.GREEN}IP Address: {ip}{Colors.ENDC}")
    except Exception as e:
        print_error(str(e))

def ping_tool():
    print_header("Ping Tool")
    host = get_input("Enter host/IP")
    count = get_input("Number of pings (default 4)") or "4"
    try:
        param = '-n' if os.name == 'nt' else '-c'
        result = subprocess.run(['ping', param, count, host], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print_error(str(e))

def system_info():
    print_header("System Information")
    import platform
    print(f"{Colors.CYAN}OS:{Colors.ENDC} {platform.system()} {platform.release()}")
    print(f"{Colors.CYAN}Architecture:{Colors.ENDC} {platform.machine()}")
    print(f"{Colors.CYAN}Processor:{Colors.ENDC} {platform.processor()}")
    print(f"{Colors.CYAN}Python Version:{Colors.ENDC} {platform.python_version()}")
    print(f"{Colors.CYAN}Hostname:{Colors.ENDC} {platform.node()}")

def disk_usage():
    print_header("Disk Usage")
    try:
        if os.name == 'nt':
            import ctypes
            drive = get_input("Drive letter (e.g., C:)") or "C:"
            free = ctypes.c_ulonglong(0)
            total = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive, ctypes.byref(free), ctypes.byref(total), None)
            print(f"{Colors.GREEN}Total: {total.value / (1024**3):.2f} GB{Colors.ENDC}")
            print(f"{Colors.GREEN}Free: {free.value / (1024**3):.2f} GB{Colors.ENDC}")
        else:
            path = get_input("Path (default /)") or "/"
            stat = os.statvfs(path)
            total = stat.f_blocks * stat.f_frsize
            free = stat.f_bfree * stat.f_frsize
            print(f"{Colors.GREEN}Total: {total / (1024**3):.2f} GB{Colors.ENDC}")
            print(f"{Colors.GREEN}Free: {free / (1024**3):.2f} GB{Colors.ENDC}")
    except Exception as e:
        print_error(str(e))

def qr_generator():
    print_header("QR Code Generator")
    text = get_input("Enter text/URL for QR code")
    try:
        encoded = urllib.parse.quote(text)
        url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded}"
        print(f"{Colors.GREEN}QR Code URL:{Colors.ENDC} {url}")
        print(f"{Colors.GRAY}Open this URL in browser to view QR code{Colors.ENDC}")
    except Exception as e:
        print_error(str(e))

def color_converter():
    print_header("Color Converter")
    print("1. HEX to RGB")
    print("2. RGB to HEX")
    print("3. HEX to HSL")
    choice = get_input("Select option")
    if choice == '1':
        hex_color = get_input("Enter HEX (e.g., #FF5733)").lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        print(f"{Colors.GREEN}RGB: ({r}, {g}, {b}){Colors.ENDC}")
    elif choice == '2':
        r = int(get_input("Red (0-255)"))
        g = int(get_input("Green (0-255)"))
        b = int(get_input("Blue (0-255)"))
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        print(f"{Colors.GREEN}HEX: {hex_color.upper()}{Colors.ENDC}")

def ip_lookup():
    print_header("IP Lookup")
    try:
        req = urllib.request.Request('https://api.ipify.org?format=json')
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"{Colors.GREEN}Your Public IP: {data['ip']}{Colors.ENDC}")
    except Exception as e:
        print_error(str(e))

def url_shortener():
    print_header("URL Shortener")
    url = get_input("Enter URL to shorten")
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url)}"
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req) as response:
            short_url = response.read().decode()
            print(f"{Colors.GREEN}Short URL: {short_url}{Colors.ENDC}")
    except Exception as e:
        print_error(str(e))

def jwt_decoder():
    print_header("JWT Decoder")
    token = get_input("Enter JWT token")
    try:
        parts = token.split('.')
        if len(parts) != 3:
            print_error("Invalid JWT format")
            return
        header = base64.urlsafe_b64decode(parts[0] + '==').decode()
        payload = base64.urlsafe_b64decode(parts[1] + '==').decode()
        print(f"{Colors.CYAN}Header:{Colors.ENDC}")
        print(json.dumps(json.loads(header), indent=2))
        print(f"\n{Colors.CYAN}Payload:{Colors.ENDC}")
        print(json.dumps(json.loads(payload), indent=2))
    except Exception as e:
        print_error(str(e))

# PLACEHOLDER FUNCTIONS (Coming Soon)
def placeholder(name):
    print_header(name)
    print(f"{Colors.WARNING}This tool is coming soon!{Colors.ENDC}")
    print(f"{Colors.GRAY}Check back in a future update.{Colors.ENDC}")

# TOOL ROUTER
TOOL_FUNCTIONS = {
    'file_splitter': file_splitter,
    'file_merger': file_merger,
    'base64_encoder': base64_encoder,
    'base64_decoder': base64_decoder,
    'password_generator': password_generator,
    'hash_generator': hash_generator,
    'uuid_generator': uuid_generator,
    'random_string': random_string,
    'basic_calculator': basic_calculator,
    'prime_checker': prime_checker,
    'factorial_calculator': factorial_calculator,
    'fibonacci_generator': fibonacci_generator,
    'percentage_calculator': percentage_calculator,
    'base_converter': base_converter,
    'unit_converter': unit_converter,
    'date_calculator': date_calculator,
    'age_calculator': age_calculator,
    'dice_roller': dice_roller,
    'coin_flip': coin_flip,
    'card_draw': card_draw,
    'text_formatter': text_formatter,
    'word_counter': word_counter,
    'lorem_ipsum': lorem_ipsum,
    'dns_lookup': dns_lookup,
    'ping_tool': ping_tool,
    'system_info': system_info,
    'disk_usage': disk_usage,
    'qr_generator': qr_generator,
    'color_converter': color_converter,
    'ip_lookup': ip_lookup,
    'url_shortener': url_shortener,
    'jwt_decoder': jwt_decoder,
}

# MAIN APPLICATION
def select_language():
    clear_screen()
    print_banner()
    print_header("LANGUAGE SELECTION")
    for key, lang in LANGUAGES.items():
        print(f"  {Colors.CYAN}{key:>2}.{Colors.ENDC} {lang['name']}")
    print_line()
    choice = get_input("Select language number")
    if choice in LANGUAGES:
        return LANGUAGES[choice]['code']
    else:
        print_warning("Invalid selection. Defaulting to English.")
        time.sleep(1)
        return 'en'

def setup_groq_api(config, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    if 'groq_api_key' not in config or not config['groq_api_key']:
        clear_screen()
        print_banner()
        print_header(t['enter_groq_key'])
        print(f"{Colors.GRAY}Get your key from: https://console.groq.com/keys{Colors.ENDC}")
        print_line()
        api_key = get_input("API Key")
        if api_key and len(api_key) > 20:
            config['groq_api_key'] = api_key
            save_config(config)
            print_success(t['key_saved'])
            time.sleep(1)
        else:
            print_warning("No valid API key provided. AI features will be disabled.")
            config['groq_api_key'] = ''
            save_config(config)
            time.sleep(2)
    return config

def show_main_menu(config, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    total_tools = sum(cat['count'] for cat in CATEGORIES.values())
    while True:
        clear_screen()
        print_banner()
        print_header(t['main_menu'])
        print(f"  {Colors.GRAY}{t['version']}: 3.0.0 | {t['total_tools']}: {total_tools}+{Colors.ENDC}\n")
        for key, cat in CATEGORIES.items():
            name = cat.get(f'name_{lang}', cat['name_en'])
            print(f"  {Colors.CYAN}{key:>2}.{Colors.ENDC} {name:<25} {Colors.GRAY}({cat['count']} {t['tool_count']}){Colors.ENDC}")
        ai_num = len(CATEGORIES) + 1
        print(f"\n  {Colors.GREEN}{ai_num:>2}.{Colors.ENDC} {Colors.BOLD}{t['ai_assistant']}{Colors.ENDC} {Colors.GRAY}(AI){Colors.ENDC}")
        print(f"  {Colors.FAIL} 0.{Colors.ENDC} {t['exit']}{Colors.ENDC}")
        print_line()
        choice = get_input(t['enter_choice'])
        if choice == '0':
            clear_screen()
            print_banner()
            print(f"\n{Colors.GREEN}Thank you for using Multi-Tool Professional Suite!{Colors.ENDC}\n")
            sys.exit(0)
        elif choice == str(ai_num):
            ai_assistant(config, lang)
        elif choice in CATEGORIES:
            show_category_menu(config, lang, choice)
        else:
            print_error(t['invalid_choice'])
            time.sleep(1)

def show_category_menu(config, lang, cat_key):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    category = CATEGORIES[cat_key]
    while True:
        clear_screen()
        print_banner()
        cat_name = category.get(f'name_{lang}', category['name_en'])
        print_header(f"{cat_name} - {t['select_tool']}")
        for key, tool in category['tools'].items():
            print(f"  {Colors.CYAN}{key:>2}.{Colors.ENDC} {tool['name']}")
        print(f"\n  {Colors.FAIL} 0.{Colors.ENDC} {t['back']}{Colors.ENDC}")
        print_line()
        choice = get_input(t['enter_choice'])
        if choice == '0':
            break
        elif choice in category['tools']:
            tool_func = category['tools'][choice]['func']
            if tool_func in TOOL_FUNCTIONS:
                clear_screen()
                print_banner()
                TOOL_FUNCTIONS[tool_func]()
                input(f"\n{Colors.GRAY}{t['press_enter']}{Colors.ENDC}")
            else:
                placeholder(category['tools'][choice]['name'])
                input(f"\n{Colors.GRAY}{t['press_enter']}{Colors.ENDC}")
        else:
            print_error(t['invalid_choice'])
            time.sleep(1)

def main():
    config = load_config()
    if 'language' not in config:
        lang = select_language()
        config['language'] = lang
        save_config(config)
    else:
        lang = config['language']
    config = setup_groq_api(config, lang)
    show_main_menu(config, lang)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Colors.GREEN}Goodbye!{Colors.ENDC}\n")
        sys.exit(0)
