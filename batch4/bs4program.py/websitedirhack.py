import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to find all the directories in the website
def find_directories(url):
    try:
        # Make a request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Unable to access {url}")
            return
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get all anchor tags from the webpage
        links = soup.find_all('a')

        # Initialize a set to store directories (to avoid duplicates)
        directories = set()

        # Loop through all links and find directories
        for link in links:
            href = link.get('href')
            if href:
                # Resolve relative URLs using urljoin
                full_url = urljoin(url, href)
                
                # Parse the URL to get the directory structure
                parsed_url = urlparse(full_url)

                # Check if the URL ends with a slash (a directory)
                if parsed_url.path.endswith('/'):
                    directories.add(full_url)

        # Print the found directories
        if directories:
            print(f"Found {len(directories)} directories on the website:")
            for directory in directories:
                print(directory)
        else:
            print("No directories found.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage: replace with the URL of the website you want to check
website_url = 'https://www.gocourse.in/2022/10/introduction-in-python.html'
find_directories(website_url)
