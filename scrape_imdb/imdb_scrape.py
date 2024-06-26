import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

# df = pd.read_csv("links.csv")
# print(df.head())

def get_movie_ids(num = 30 , page = 1):
    links_data = pd.read_csv("links.csv")
    movie_ids = list(links_data.imdbId)
    start_index = (page - 1) * num
    end_index = start_index + num
    return movie_ids[start_index:end_index]

def scrape_movie_index_page(movie_id):
    movie_index_url = "https://www.imdb.com/title/tt{}".format(str(movie_id).zfill(7))
    current_page = requests.get(movie_index_url)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    current_page = requests.get(movie_index_url, headers=header)
    # print(current_page.text)  # Print the response content
    index_soup = BeautifulSoup(current_page.text , "html.parser")
    current_page_json = index_soup.find("script" , attrs= {"type" : "application/ld+json"})
    current_page_json = str(current_page_json)[str(current_page_json).find('{'):-9]
    return current_page_json


def collect_movie_dict(movie_id):
    page_json = json.loads(scrape_movie_index_page(movie_id))
    movie = {
        "name": page_json["name"],
        "genre": page_json["genre"],
        "image": page_json["image"],
        "description": page_json["description"]
    }
    print(movie["name"])
    return movie

def get_movies_paged(page=2 , movie_per_page=10):
    ids = get_movie_ids(num= movie_per_page, page=page)
    scrape_result = {"movies":[]}
    for id in ids:
        scrape_result["movies"].append(collect_movie_dict(id))
    return scrape_result

if __name__ == "__main__":
    ids = get_movie_ids(10)
    print(ids)
    for x in ids:
        collect_movie_dict(x)