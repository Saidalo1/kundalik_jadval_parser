import logging
import os

from PIL import Image
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

from functions import date

load_dotenv('.env')
LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

logging.basicConfig(level=logging.INFO)


def main():
    # Open Chrome browser
    driver = webdriver.Chrome()

    # To maximize the browser window
    driver.maximize_window()

    # Get URL of website
    driver.get("https://login.kundalik.com/login")

    # Find login input field
    login = driver.find_element(By.NAME, "login")

    # Write username to login field
    login.send_keys(f'{LOGIN}')

    # Find password input field
    password = driver.find_element(By.NAME, "password")

    # Write password to password field
    password.send_keys(f'{PASSWORD}')

    # Click submit
    password.submit()

    # Save today's date to mutable objects
    year = date('%Y')
    month = date('%m')
    day = date('%d')

    # Login to timetable url
    driver.get(f'https://kundalik.com/user/calendar.aspx?year={year}&month={month}&day={day}')

    # Get path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Find element of today table
    table = driver.find_element(By.XPATH, "//div[@class='col34 first']")

    # Get the element location
    location = table.location

    # Size
    size = table.size

    # Save screenshot
    driver.save_screenshot("time_table.png")

    # to get the x axis
    x = location['x']

    # to get the y axis
    y = location['y']

    # to get the length the element
    height = location['y'] + size['height']

    # to get the width the element
    width = location['x'] + size['width']

    # to open the captured image
    img_open = Image.open("time_table.png")

    # to crop the captured image to size of that element
    img_open = img_open.crop((int(x), int(y), int(width), int(height)))

    # to save the cropped image
    img_open.save("time_table.png")

    # to close the browser
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
