# Import the required modules
from bs4 import BeautifulSoup

# Sample HTML content (you can replace this with real HTML from a website)
html = '''
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1 id="main-title">Welcome!</h1>
    <p class="description">This is a test paragraph.</p>
    <a href="https://example.com">Visit Example</a>
    <a href="https://openai.com">OpenAI</a>
  </body>
</html>
'''

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the <title> tag and its text
title_tag = soup.title
print("Title Tag:", title_tag)
print("Title Text:", title_tag.string)

# Extract the <h1> tag and its id
h1_tag = soup.find('h1')
print("\nH1 Tag:", h1_tag)
print("H1 Text:", h1_tag.text)
print("H1 ID:", h1_tag['id'])

# Extract the <p> tag with class "description"
p_tag = soup.find('p', class_='description')
print("\nParagraph Tag:", p_tag)
print("Paragraph Text:", p_tag.text)

# Extract all <a> tags and their hrefs
a_tags = soup.find_all('a')
print("\nAll Links:")
for a in a_tags:
    print(f"Text: {a.text}, Href: {a['href']}")
