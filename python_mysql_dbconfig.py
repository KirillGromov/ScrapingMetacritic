from configparser import ConfigParser
import log

def read_db_config(filename='C:\\Users\\Womorg\\Desktop\\CTF\\Metacritics\\config.ini', section='mysql'):

    parser = ConfigParser()
    parser.read(filename)


    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        
        for item in items:
            db[item[0]] = item[1]
    else:
        log.logging.error(f'{section} not found in the {filename} file')
        raise Exception('{0} not found in the {1} file'.format(section, filename))
        

    return db