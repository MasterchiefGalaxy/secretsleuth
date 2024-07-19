PATTERNS = {
    'hardcoded_secrets': [
        r'password\s*=\s*["\'][^"\']+["\']',
        r'api_key\s*=\s*["\'][^"\']+["\']',
        r'username\s*=\s*["\'][^"\']+["\']',
        # Add more patterns as needed
    ]
}
