from scanner import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SecretSleuth - Mobile Application Security Testing Tool")
    parser.add_argument('target', help='Path to the IPA or APK file')
    args = parser.parse_args()

    main(args.target)
