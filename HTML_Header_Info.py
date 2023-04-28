#This script will scrape all the suspicous header info from the given URL.
import requests

url = input("Enter the URL: ")
response = requests.get(url)

# List of suspicious headers
suspicious_headers = ['Content-Encoding', 'Content-Length', 'Content-Type', 'Server', 'X-Powered-By', 'X-AspNet-Version', 'X-AspNetMvc-Version']

# Check for suspicious headers
for header in response.headers:
    if header in suspicious_headers:
        print("Suspicious header found:", header, ":", response.headers[header])

# Print message if no suspicious headers found
if not any(header in response.headers for header in suspicious_headers):
    print("No suspicious headers found.")

