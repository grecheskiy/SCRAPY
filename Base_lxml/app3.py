import requests
from lxml import html
import pandas as pd

resp = requests.get(url='https://www.imdb.com/list/ls054383657/?ref_=login', 
                    headers= {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

tree = html.fromstring(html=resp.content)
print(resp)

transfers = tree.xpath("//div[@class='lister-list']/div")

all_transfers = []
for tran in transfers:
    tran={
        'Number_#' : tran.xpath(".//div[@class='lister-item-content']/h3/span[@class='lister-item-index unbold text-primary']/text()"),
        'Name' : tran.xpath(".//div[@class='lister-item-content']/h3/a/text()"),
        'Realise_year' : tran.xpath(".//div[@class='lister-item-content']/h3/span[@class='lister-item-year text-muted unbold']/text()"),
        'Certificate' : tran.xpath(".//div[@class='lister-item-content']/p[1]/span[1]/text()"),
        'Genre' : tran.xpath(".//div[@class='lister-item-content']/p[1]/span[3]/text()"),
        'Rating' : tran.xpath(".//div[@class='lister-item-content']/div[1]/div[1]/span[2]/text()")
        }
    all_transfers.append(tran)

print(all_transfers)
print(len(all_transfers))

df = pd.DataFrame(all_transfers)
df.to_csv("Base_lxml/best_games.csv")