import logging
# import os

# create logger
logging.basicConfig(
    filename='python.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S'
)

# logger = logging.getLogger('hotel')
# # create file handler which logs even info messages
# file_log = logging.FileHandler(os.path.join(os.getcwd(), 'python.log'))

# # create console handler with a higher log level
# console_log = logging.StreamHandler()
# # create formatter and add it to the handlers
# formatter = logging.Formatter(
#
# )
# file_log.setFormatter(formatter)
# console_log.setFormatter(formatter)

# # add the handlers to the logger
# logger.addHandler(file_log)
# logger.addHandler(console_log)
