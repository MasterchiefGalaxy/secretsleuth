from ipa_scanner import scan_ipa
from apk_scanner import scan_apk
from reporter import generate_report

def main(target_path):
    if target_path.endswith('.ipa'):
        findings = scan_ipa(target_path)
    elif target_path.endswith('.apk'):
        findings = scan_apk(target_path)
    else:
        print("Unsupported file type")
        return

    generate_report(findings)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
