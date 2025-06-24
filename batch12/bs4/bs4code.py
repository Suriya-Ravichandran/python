import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Target URL
url = "https://google.com"

# Directory to save the clone
output_dir = "website_clone"
os.makedirs(output_dir, exist_ok=True)

# Download helper
def download_file(session, file_url, folder):
    parsed_url = urlparse(file_url)
    file_name = os.path.basename(parsed_url.path)
    if not file_name:
        return None

    local_path = os.path.join(folder, file_name)
    os.makedirs(folder, exist_ok=True)

    try:
        response = session.get(file_url, timeout=10)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_url} → {local_path}")
            return os.path.relpath(local_path, output_dir)
    except Exception as e:
        print(f"Failed to download {file_url}: {e}")
    return None

# Start session
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

# Download main page
response = session.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Tags and attributes to look for assets
asset_tags = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}

# Download and replace asset links
for tag, attr in asset_tags.items():
    for element in soup.find_all(tag):
        asset_url = element.get(attr)
        if asset_url and not asset_url.startswith("data:"):
            full_url = urljoin(url, asset_url)
            folder = os.path.join(output_dir, tag)
            local_rel_path = download_file(session, full_url, folder)
            if local_rel_path:
                element[attr] = local_rel_path.replace("\\", "/")

# Save the modified HTML
html_path = os.path.join(output_dir, "index.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"\n✅ Website cloned successfully to: {html_path}")
