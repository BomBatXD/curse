import os
import creds
import requests
import time


virus_total_api_scan_url = "https://www.virustotal.com/api/v3/files"
virus_total_get_report_url = "https://www.virustotal.com/api/v3/analyses"
virus_total_api_key = creds.api_key


def upload_file(file_path):
    headers = {"x-apikey": virus_total_api_key}
    with open(file_path, 'rb') as f:
        files = {"file": (file_path, f)}
        response = requests.post(virus_total_api_scan_url, files=files, headers=headers)
        if response.status_code != 200:
            print(f"\nError uploading {file_path}:\n{response.text}")
            # If it's a rate or conflict error, wait and retry
            if response.status_code == 429 or 'ConflictError' in response.text:
                print("Rate limited or conflict. Waiting 30 seconds and retrying...")
                time.sleep(30)
                return upload_file(file_path)
            raise Exception(f"Error from VirusTotal: {response.status_code}")
        return response.json()['data']['links']['self']

def scan_folder_files(folder_path):
    if os.path.exists():
        for item in os.listdir(folder_path):
            full_item_path = os.path.join(folder_path, item)
            if os.path.isdir(full_item_path):
                scan_folder_files(full_item_path)
            else:
                scan_file(full_item_path)
                time.sleep(20) # For the scan to work
            

def scan_file(file_path):
    url = upload_file(file_path)
    is_virus = get_report(url)
    if is_virus:
        print(f"{file_path:<70} is a virus")
    else:
        print(f"{file_path:<70} is not a virus")

def get_report(url):
    headers = {"x-apikey": virus_total_api_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.text)
        raise Exception("Unexpected error in response")
    result = response.json()
    detections = result['data']['attributes']['stats']
    return detections['malicious'] > 0 or detections['suspicious'] > 0


def main():
    scan_folder_files(r"C:\Users\yehon\Desktop\MOAF\minecraft")


if __name__ == '__main__':
    main()