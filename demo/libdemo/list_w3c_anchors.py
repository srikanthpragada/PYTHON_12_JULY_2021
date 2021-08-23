from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

for a in bs.find_all("a"):
    text = a.text.strip()
    if len(text) == 0:
        continue

    href = a['href']
    if href == '#':
        continue

    if 'javascript:void' in href:
        continue

    print(text)
    if href.startswith("http"):
        print(href)
    else:
        print(WEBSITE + "/" + href)
