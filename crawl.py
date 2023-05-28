import requests
from bs4 import BeautifulSoup


url = 'https://www.besoccer.com'
response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')

# links = soup.select('a.match-link')

# # Find all <a> tags and print their href attributes
# for link in soup.find_all('a'):
#         print(link.prettify())


# Assume `soup` is the BeautifulSoup object containing the parsed HTML

# Find all <a> tags with class "my-link" and print their text
imgs = soup.select('img.player')
for img in imgs:
    print(img.prettify())



# Find all <a> tags with class "match-link" and save their HTML representation to an index.html file
# links = soup.select('a.match-link')

# with open('index.html', 'w', encoding='utf-8') as file:
#     for link in links:
#         file.write(link.prettify())
#         file.write('\n')  # Add a newline after each element

# print("HTML content saved to index.html")