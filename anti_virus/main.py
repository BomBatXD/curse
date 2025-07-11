import os
import creds
import requests
import time
import threading
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

virus_total_api_scan_url = "https://www.virustotal.com/api/v3/files"
virus_total_api_key = creds.api_key

def upload_file(file_path, log_func):
    headers = {"x-apikey": virus_total_api_key}
    with open(file_path, 'rb') as f:
        files = {"file": (file_path, f)}
        response = requests.post(virus_total_api_scan_url, files=files, headers=headers)
        if response.status_code != 200:
            log_func(f"Error uploading {file_path}: {response.text}\n")
            # If it's a rate or conflict error, wait and retry
            if response.status_code == 429 or 'ConflictError' in response.text:
                log_func("Rate limited or conflict. Waiting 30 seconds and retrying...\n")
                time.sleep(30)
                return upload_file(file_path, log_func)
            raise Exception(f"Error from VirusTotal: {response.status_code}")
        return response.json()['data']['links']['self']

def get_report(url, log_func):
    headers = {"x-apikey": virus_total_api_key}
    for _ in range(15):  # Try up to ~90 seconds (15 * 6)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            log_func(f"Error retrieving report: {response.text}\n")
            time.sleep(6)
            continue
        result = response.json()
        if result['data']['attributes']['status'] == 'completed':
            detections = result['data']['attributes']['stats']
            return detections['malicious'] > 0 or detections['suspicious'] > 0
        else:
            time.sleep(6)
    log_func("Timeout waiting for report.\n")
    return False

def scan_file(file_path, log_func):
    try:
        url = upload_file(file_path, log_func)
        is_virus = get_report(url, log_func)
        if is_virus:
            log_func(f"{file_path:<70} is a VIRUS\n")
        else:
            log_func(f"{file_path:<70} is not a virus\n")
    except Exception as e:
        log_func(f"{file_path:<70} Error: {e}\n")

def scan_folder_files(folder_path, log_func, stop_event):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if stop_event.is_set():
                log_func("Scan stopped by user.\n")
                return
            full_item_path = os.path.join(root, file)
            scan_file(full_item_path, log_func)
            time.sleep(20)  # To avoid rate limits

class VirusScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTotal Folder Scanner")
        self.root.geometry("750x500")

        self.folder_path = tk.StringVar()
        self.stop_event = threading.Event()
        self.scan_thread = None

        tk.Label(root, text="Folder:").pack(anchor='w', padx=10, pady=5)
        path_frame = tk.Frame(root)
        path_frame.pack(fill='x', padx=10)
        tk.Entry(path_frame, textvariable=self.folder_path, width=60).pack(side='left', fill='x', expand=True)
        tk.Button(path_frame, text="Browse", command=self.browse_folder).pack(side='left', padx=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(fill='x', padx=10, pady=5)
        self.scan_btn = tk.Button(btn_frame, text="Start Scan", command=self.start_scan)
        self.scan_btn.pack(side='left')
        self.stop_btn = tk.Button(btn_frame, text="Stop Scan", command=self.stop_scan, state='disabled')
        self.stop_btn.pack(side='left', padx=5)

        self.log = scrolledtext.ScrolledText(root, wrap='word', height=22, font=('Consolas', 10))
        self.log.pack(fill='both', expand=True, padx=10, pady=10)

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path.set(path)

    def log_func(self, message):
        self.log.insert(tk.END, message)
        self.log.see(tk.END)
        self.root.update_idletasks()

    def start_scan(self):
        folder = self.folder_path.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid folder.")
            return
        self.scan_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.stop_event.clear()
        self.log_func(f"Starting scan in: {folder}\n")
        self.scan_thread = threading.Thread(target=scan_folder_files, args=(folder, self.log_func, self.stop_event))
        self.scan_thread.start()

    def stop_scan(self):
        self.stop_event.set()
        self.scan_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.log_func("Stopping scan...\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirusScannerGUI(root)
    root.mainloop()
