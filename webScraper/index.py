import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com")

print(result.status_code)
# print(result.headers)
print("\n")

src = result.content

soup = BeautifulSoup(src, 'html.parser')
links = soup.find_all("a", class_="gb1")

# print(links)

for link in links:
    if "Grafika" in link.text:
        print(link)
        print("\n")
        print(link.attrs["href"])
        print(link.attrs["class"])