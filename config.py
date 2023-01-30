from os import getenv

from dotenv import load_dotenv

load_dotenv()

# import database settings from .env file
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_USER = getenv('DATABASE_USER')
DATABASE_PASS = getenv('DATABASE_PASS')
DATABASE_HOST = getenv('DATABASE_HOST')
