import json
import cfscrape
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium_open_site import get_sourse_html

url = 'https://yandex.ru/maps/?ll=52.583698%2C56.067155&z=5.86'


# def get_session():
#     session = requests.Session()
#     session.headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#         'upgrade-insecure-requests': '1',
#         # 'user-agent': useragent.random,
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#         'viewport-width': '1920'
#     }
#     return cfscrape.create_scraper(sess=session)

# url = 'https://yandex.ru/maps/?display-text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&ll=50.417027%2C55.287521&mode=search&page=3&sctx=ZAAAAAgBEAAaKAoSCVmis8wixklAEVK4HoXrPUtAEhIJYOemzTgNkT8RbsST3cyIHUAiBgABAgMEBSgKOABA71ZIAWIRb2JqZWN0c19kaXNhYmxlPTFqAnJ1nQHNzEw9oAEAqAEAvQGi8zndwgGCAdazkMqjBb7X3dMEg%2FCYhQTZ0%2F%2BIBKnl8%2BSNBZXT9cMEusLLngSl9cvABImEooUE0s%2FbqgTet5zeBqKNtYMEl%2FLZygTip6fzBIz7gceUA%2FDVjrYE6%2FTfzATS9oXY1QHWo6KtBNPw9r4E3M2LrATzgpieBMLToq4ErqiHu2baqOatjAPqAQDyAQD4AQCCAhTRgtCw0YLRgtC10LvQtdC60L7QvIoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=50.417027%2C55.287521&sspn=8.081710%2C4.154782&text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&z=7.2'
# session = get_session()
# r = session.get(url)

data_result = {
    'company_info': {}
}


def get_count_star(review_stars):
    star_count = 0
    for review_star in review_stars:
        if '_empty' in review_star.get('class'):
            continue
        elif '_half' in review_star.get('class'):
            star_count = star_count + 0.5
        else:
            star_count = star_count + 1
    return star_count


def parsing_data():
    test = open('test.html', encoding="utf-8")


    soup = BeautifulSoup(test, 'lxml')
    try:
        reviews = soup.find_all('li', {"class": "search-snippet-view"})
    except:
        return None
    # try:
        # tag = reviews.find('div', {"class": 'search-snippet-view__body _type_business'})
    # except:
    #     return None

    for i in range(len(reviews)):
        id_filials = reviews[i].find('div', {"class": 'search-snippet-view__body _type_business'})
        id_filials = id_filials['data-id']
        address = reviews[i].find('div', {"class": 'search-business-snippet-view__address'}).text
        average_mark = reviews[i].find('span', {"class": 'business-rating-badge-view__rating-text _size_m'}).text
        total_marks = reviews[i].find('span', {"class": 'business-rating-amount-view'}).text
        stars_summary_rating__main = reviews[i].find('div', {"class": "business-rating-badge-view__stars"})
        sum_stars = stars_summary_rating__main.find_all('span', {
            "class": "inline-image _loaded business-rating-badge-view__star _full _size_m"})

        print(len(sum_stars))

        print (address)
        print(id_filials)
        print (average_mark)
        print (total_marks)
        print(len(sum_stars))


def main():
    get_sourse_html(url=url)
    #parsing_data()


if __name__ == "__main__":
    main()
