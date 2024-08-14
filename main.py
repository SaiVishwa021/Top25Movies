import requests
from bs4 import BeautifulSoup
import json
import datetime
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)

def fetch_imdb_top_25(year, headers):
    url = f"http://www.imdb.com/search/title?release_date={year}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    dataset_top25 = {}
    movies_list = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-748571c8-0 jApQAb detailed-list-view ipc-metadata-list--base')
    
    if not movies_list:
        print(f"No movies found for the year {year}")
        return None
    
    li_items = movies_list.find_all('li', class_="ipc-metadata-list-summary-item")
    for idx, each in enumerate(li_items, start=1):
        movie_item = {
            'name': each.find('h3', class_='ipc-title__text').text.strip() if each.find('h3', class_='ipc-title__text') else 'N/A',
            'rating': each.find('span', class_='ipc-rating-star--rating').text.strip() if each.find('span', class_='ipc-rating-star--rating') else 'N/A',
            'description': each.find('div', class_='ipc-html-content-inner-div').text.strip() if each.find('div', class_='ipc-html-content-inner-div') else 'N/A'
        }
        dataset_top25[idx] = movie_item
    
    return dataset_top25

def save_to_json(data, year):
    if data:
        with open(f'DataSets/IMDB_Top_25_{year}.json', 'w') as f:
            json.dump(data, f, indent=4)
        
def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    current_year = datetime.datetime.now().year

    for year in range(1950, current_year + 1):
        sys.stdout = open(f'DataSets/IMDB_Top_25_{year}.json', 'w')
        dataset_top25 = fetch_imdb_top_25(year, headers)
        save_to_json(dataset_top25, year)

if __name__ == '__main__':
    main()
