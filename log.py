import logging

logging.basicConfig(
    filename='app.log', 
    filemode='w', 
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)