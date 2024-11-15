import requests

# Define the URL
url = "https://ycharts.com/companies/TSLA/revenues"

# Define headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Make a GET request with headers
response = requests.get(url, headers=headers)

# Check the status code of the response
print(response.status_code)

# If successful, print the first few characters of the HTML content
if response.status_code == 200:
    print(response.text[:500])  # Display the first 500 characters of the HTML content
else:
    print("Request was denied. Status code:", response.status_code)

