import requests
import sys

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    variable = sys.argv[1]
else:
    print("Nebyla zadána žádná proměnná.")
    exit(1)

# WordPress REST API endpoint
url = "https://it2405.sspu-opava.eu/wp-json/wp/v2/posts"

# Authentication credentials (replace with your actual username and application password)
username = "dvorak"
password = "3KsY 64zD T8bG Scuj yKux htMQ"

# Post data
data = {
    "title": variable,  # Use the command-line argument as the post title
    "content": "dnes je ctvrtek",
    "status": "publish"  # Publish the post immediately
}

# Send POST request to WordPress REST API
response = requests.post(url, json=data, auth=(username, password))

# Check response
if response.status_code == 201:  # 201 Created
    print("Post created successfully!")
    print("Post ID:", response.json().get("id"))
else:
    print("Failed to create post.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
