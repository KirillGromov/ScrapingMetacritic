from bs4 import BeautifulSoup
import requests
from python_mysql_connect2 import connect, insert_film
import log
import mysql
import mysql.connector



class Film():


    '''Обозначение структуры данных'''
    def __init__(self, name, picture, date, score, mppa, html):
        self.name = name
        self.picture = picture
        self.date = date
        self.score = score
        self.mppa = mppa
        self.html = html


    '''Нахождение пагинации'''
    def get_pages_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find_all('a', class_='page_num')
        if pagination:
            pages_count = pagination[-1].get_text()
            log.logging.info(f'Count pages: {pages_count}')
            return int(pagination[-1].get_text())
        else:
            log.logging.info(f'Count pages: {1}')
            return 1



    def get_content(self, html):

        '''Выборка нужных элементов для записи в БД'''

        '''Выбор нужного участка (элемента) страницы'''
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('td', class_='clamp-summary-wrap')
        items_picture = soup.find_all('td', class_='clamp-image-wrap')
        
        '''Выборка и запись'''
        for item in items:
            film = Film('name', 'picture', 'date', 'score', 'mppa', html)
            film.name = item.find('a', class_='title').get_text(strip=True)
            for itemn in items_picture:
                film.picture = itemn.find('img').get('src')
            film.score = item.find('div', class_='metascore_w').get_text(strip=True)
            film.date = item.find('div', class_='clamp-details').find_next('span').get_text(strip=True)
            if item.find('span', class_='cert_rating'):
                film.mppa = item.find('span', class_='cert_rating').get_text(strip=True)
            else:
                film.mppa = '| Not Rated'
            insert_film(film.name, film.picture, film.date, film.score, film.mppa)

        return 1