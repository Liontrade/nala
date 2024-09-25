import requests
from bs4 import BeautifulSoup
import json


def fetch_sp500_symbols():
    url = 'https://www.slickcharts.com/sp500'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to load page {url} - Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    symbols = []

    table = soup.find('table', {'class': 'table table-hover table-borderless table-sm'})

    if table is None:
        raise Exception("Failed to find the table on the page")

    for row in table.find_all('tr')[1:]:
        symbol = row.find_all('td')[2].text.strip()
        symbols.append(symbol)

    # Zapisanie symboli do pliku JSON
    with open('symbols.json', 'w') as f:
        json.dump(symbols, f)


if __name__ == '__main__':
    fetch_sp500_symbols()
