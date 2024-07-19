import zipfile
import os
from file_scanner import scan_file

def extract_apk(file_path, extract_to='extracted_apk'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def scan_apk(file_path):
    print("Extracting APK...")
    extracted_path = extract_apk(file_path)
    findings = []
    print("Scanning files...")
    for root, _, files in os.walk(extracted_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning file: {file_path}")
            findings.extend(scan_file(file_path))
    print(f"Found {len(findings)} issues.")
    return findings
