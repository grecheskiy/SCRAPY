import requests
from lxml import html
from pymongo import MongoClient

def insert_to_db(list_movies):
    client = MongoClient("mongodb://localhost:27017")
    db = client["imdb_movies"]
    collection = db["top_movies"]
    collection.insert_many(list_movies)
    client.close()

resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm', 
                    headers= {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

tree = html.fromstring(html=resp.content)
print(resp)

movies = tree.xpath("//ul[@role='presentation']/li/div[@class='ipc-metadata-list-summary-item__c']/div[@class='ipc-metadata-list-summary-item__tc']/div[@class='sc-b0691f29-0 jbYPfh cli-children']")

all_movies = []
for movie in movies:
    m={
        'name' : movie.xpath(".//div[@class='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title']/a/h3/text()")[0],
        'release_year' : movie.xpath(".//div[@class='sc-b0691f29-7 hrgukm cli-title-metadata']/span[1]/text()"),
        'long_time' : movie.xpath(".//div[@class='sc-b0691f29-7 hrgukm cli-title-metadata']/span[2]/text()"),
        'title_meter' : movie.xpath(".//div[@class='sc-b0691f29-7 hrgukm cli-title-metadata']/span[3]/text()"),
        'posision' : movie.xpath(".//span/div/span/text()")}
    all_movies.append(m)

insert_to_db(all_movies)
#print(all_movies)
#print(len(all_movies))
