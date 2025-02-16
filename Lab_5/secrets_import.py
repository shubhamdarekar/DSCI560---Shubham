import configparser
config = configparser.ConfigParser()
config.read('/home/shubhamdarekar/DSCI560---Shubham/Lab_5/.env')

MYSQL_HOST=config['mysql']['host']
MYSQL_USER = config['mysql']['user']
MYSQL_PASSWORD = config['mysql']['password']
MYSQL_DB = config['mysql']['database']