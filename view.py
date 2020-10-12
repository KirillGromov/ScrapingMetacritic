import model
from contoller import play_parser
import log



def main():
    URL = input('Введите ссылку на сайт с фильмами: ')
    URL = URL.strip()
    log.logging.info(f'Programm started')
    play_parser(URL)
    log.logging.info(f'Programm exit')



main()