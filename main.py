#!/usr/bin/env python3

import os
import sys
import subprocess
import time
from pathlib import Path

VERSION = "1.0"
DEVELOPER = "@ERROR0101risback"
CHANNEL = "https://t.me/aab_ho_ga_comeback"

def c(text, color):
    colors = {'r': '\033[91m', 'g': '\033[92m', 'y': '\033[93m', 'b': '\033[94m', 'p': '\033[95m', 'c': '\033[96m', 'end': '\033[0m'}
    return f"{colors.get(color, '')}{text}{colors['end']}"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = f"""
{c('█'*60, 'r')}
{c('█' + ' '*58 + '█', 'r')}
{c('█' + '* '*19 + ' ERROR ENCRYPTOR TOOL ' + '* '*19 + '█', 'r')}
{c('█' + ' '*58 + '█', 'r')}
{c('█'*60, 'r')}
"""
    print(banner)
    print(c(f"\n{c('Developer:', 'c')} {DEVELOPER}", 'g'))
    print(c(f"{c('Channel:', 'c')} {CHANNEL}", 'g'))
    print()

def check_requirements(tool_name):
    if tool_name == 'html':
        try:
            __import__('Crypto')
            print(c("✅ pycryptodome already installed", 'g'))
            return True
        except ImportError:
            print(c("📦 Installing pycryptodome...", 'y'))
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
                print(c("✅ pycryptodome installed successfully", 'g'))
                return True
            except:
                print(c("❌ Failed to install pycryptodome", 'r'))
                return False
    return True

def run_script(script_name):
    if not os.path.exists(script_name):
        print(c(f"❌ Script not found: {script_name}", 'r'))
        return False
    
    print(c(f"\n🚀 Running {script_name}...\n", 'c'))
    try:
        subprocess.run([sys.executable, script_name])
        return True
    except KeyboardInterrupt:
        print(c("\n\n❌ Cancelled by user", 'r'))
        return False
    except Exception as e:
        print(c(f"❌ Error: {e}", 'r'))
        return False

def main():
    while True:
        clear_screen()
        print_banner()
        
        print(c("═"*50, 'y'))
        print(c("📌 MAIN MENU", 'c'))
        print(c("═"*50, 'y'))
        print()
        print(c("  [1] 🔒 HTML ENCRYPTOR", 'g'))
        print(c("  [2] 🐍 PYTHON ENCRYPTOR", 'g'))
        print(c("  [3] ❌ EXIT", 'r'))
        print()
        
        choice = input(c("👉 Enter your choice (1-3): ", 'c')).strip()
        
        if choice == '1':
            clear_screen()
            print_banner()
            print(c("🔒 Starting HTML Encryptor...\n", 'y'))
            if check_requirements('html'):
                time.sleep(1)
                run_script("Error_html_encryptor.py")
            else:
                print(c("\n❌ Requirements not met. Press Enter to continue...", 'r'))
                input()
        
        elif choice == '2':
            clear_screen()
            print_banner()
            print(c("🐍 Starting Python Encryptor...\n", 'y'))
            time.sleep(1)
            run_script("Error_encryptor.py")
        
        elif choice == '3':
            clear_screen()
            print(c("\n👋 Thank you for using ERROR ENCRYPTOR TOOL!", 'c'))
            print(c(f"📢 Channel: {CHANNEL}", 'c'))
            print(c(f"👨‍💻 Developer: {DEVELOPER}\n", 'c'))
            sys.exit(0)
        
        else:
            print(c("\n❌ Invalid choice! Press Enter to continue...", 'r'))
            input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c("\n\n❌ Cancelled by user", 'r'))
        sys.exit(0)