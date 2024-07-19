import zipfile
import os
from file_scanner import scan_file

def extract_ipa(file_path, extract_to='extracted_ipa'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def scan_ipa(file_path):
    print("Extracting IPA...")
    extracted_path = extract_ipa(file_path)
    findings = []
    print("Scanning files...")
    for root, _, files in os.walk(extracted_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning file: {file_path}")
            findings.extend(scan_file(file_path))
    print(f"Found {len(findings)} issues.")
    return findings
