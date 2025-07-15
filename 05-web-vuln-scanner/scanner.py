import requests

# Check for directory listing on a given path
def check_directory_listing(url):
    response = requests.get(url)
    if "Index of" in response.text:
        print("[!] Directory listing detected!")
    else:
        print("[+] No directory listing detected.")

# Check if dangerous HTTP methods are allowed
def check_http_methods(url):
    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    for method in methods:
        response = requests.request(method, url)
        if response.status_code < 400:
            print(f"[!] {method} method is allowed.")
    print("[+] Checked HTTP methods.")

# Check for missing security headers
def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    if "X-Frame-Options" not in headers:
        print("[!] Missing X-Frame-Options header.")
    if "Content-Security-Policy" not in headers:
        print("[!] Missing Content-Security-Policy header.")
    if "Strict-Transport-Security" not in headers:
        print("[!] Missing Strict-Transport-Security header.")
    print("[+] Checked security headers.")

if __name__ == "__main__":
    target = input("Enter target URL (e.g., http://example.com): ")
    check_directory_listing(target)
    check_http_methods(target)
    check_security_headers(target)