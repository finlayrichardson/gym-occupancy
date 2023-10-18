import re
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime


def get_occupancy() -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get("https://sport.wp.st-andrews.ac.uk/", headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.findAll('div', {'class': 'col-sm-6 content'})
    occupancy = re.search('\d*%', str(content[1]))
    occupancy = occupancy.group(0).strip("%")
    return occupancy


f = open("results.json", "r")
data = json.loads(f.read())
f.close()
now = datetime.now()
data[now.strftime("%A")][now.strftime("%H:%M")] = get_occupancy()
json = json.dumps(data)
f = open("results.json", "w")
f.write(json)
f.close()
