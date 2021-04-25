import requests
from bs4 import BeautifulSoup
import pandas as pd

datalist = []
def pages(page):
    url = f'https://scholar.google.com/scholar?start={x}&q=egfr+mutation&hl=en&as_sdt=0,5'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    h_tags = soup.find_all('h3', {'class' : 'gs_rt'})

    for tag in h_tags:
        titles = tag.get_text().replace('[HTML]', '').strip()
        data = {
        'titles' : titles        
        }   
        datalist.append(data)
        print(datalist)

for x in range(1, 10):
    pages(x)
    
df = pd.DataFrame(datalist)
df.to_excel('google5.xlsx', index=None)
print('file downloaded:..')