from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = "https://www.livewireindia.in"

# Fetch the content of the webpage
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all hyperlinks (anchor tags)
    links = soup.find_all('a')

    head=soup.find("head")
    f=open("livewirehead.html","w")
    f.write(str(head))

    print("List of Hyperlinks:")
    for link in links:
        href = link.get('href')  # Get the href attribute
        if href:
            print(href)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")