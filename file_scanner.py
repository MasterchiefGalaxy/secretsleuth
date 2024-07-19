import re
from config import PATTERNS

def scan_file(file_path):
    findings = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        for name, patterns in PATTERNS.items():
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    print(f"Found match: {match} in file: {file_path}")
                    findings.append({
                        'type': name,
                        'pattern': pattern,
                        'match': match,
                        'file': file_path
                    })
    return findings

# Test the scan_file function with test_file.txt
if __name__ == "__main__":
    test_findings = scan_file('test_file.txt')
    print(test_findings)
