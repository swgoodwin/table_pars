import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['price']))



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='cmc-link').text
        price = tds[3].find('a').text[1:]
        print(name, price)

        data = {'name': name,
                'price': price}

        write_csv(data)



def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))

if __name__ == '__main__':
    main()