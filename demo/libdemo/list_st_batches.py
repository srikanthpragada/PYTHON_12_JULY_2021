from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')
sch_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = sch_table.find_all("tr")[1:]
for row in rows:
    cols = row.find_all('td')
    name = cols[0].text
    anchor = cols[0].find("a")
    href = anchor['href']
    timings = cols[1].text
    stdate = cols[2].text
    href = WEBSITE + "/" + href
    print(f"{name:20} {stdate:10} {timings:10} {href}")



