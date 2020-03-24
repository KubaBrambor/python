import requests
from bs4 import BeautifulSoup

# result = requests.get("https://www.google.com")

# print(result.status_code)
# # print(result.headers)
# print("\n")

# src = result.content

# soup = BeautifulSoup(src, 'html.parser')
# links = soup.find_all("a", class_="gb1")

# # print(links)

# for link in links:
#     if "Grafika" in link.text:
#         print(link)
#         print("\n")
#         print(link.attrs["href"])
#         print(link.attrs["class"])

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = result.content
soup = BeautifulSoup(src, 'html.parser')
print(soup.prettify())

# urls = []

# for h2_tag in soup.find_all("h2"):
#     a_tag = h2_tag.find("a")
#     urls.append(a_tag.attrs["href"])

# for url in urls:
#     print(url)
