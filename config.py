from os import getenv

from dotenv import load_dotenv

from functions import date

load_dotenv()

# import telegram bot settings from .env file
TOKEN = getenv('TOKEN')

# import database settings from .env file
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_USER = getenv('DATABASE_USER')
DATABASE_PASS = getenv('DATABASE_PASS')
DATABASE_HOST = getenv('DATABASE_HOST')

# Date
year = date('%Y')
month = date('%m')
day = date('%d')
week_day = date('%w')
