import log
import model
from configparser import ConfigParser
from python_mysql_connect2 import query_last_film



HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 'accept': '*/*'}



def get_html(url, params = None):
    r = model.requests.get(url, headers = HEADERS, params=params)
    return r



def play_parser(URL):
    html = get_html(URL)
    if html.status_code == 200:
        log.logging.info(f'Status code {html.status_code}')

        a = model.Film('name', 'picture', 'date', 'score', 'mppa', html)
        pages_count = a.get_pages_count(html.text)

        for page in range(1, pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            a.get_content(html.text)
            html = get_html(URL, params={'page': page})

    else:
        log.logging.error(f'Status code {html.status_code}')
        print("Такая страница не найдена")
    
    last_film = query_last_film()

    log.logging.info(f'Last film:  {last_film}')
    return 1