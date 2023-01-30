import logging
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

from functions import date
from models import session, Schedule

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
    week_day = date('%w')

    # Login to timetable url
    driver.get(f'https://kundalik.com/user/calendar.aspx?year={year}&month={month}&day={day}')

    # Find lesson schedule for today
    schedule_elements = driver.find_elements(By.XPATH, "//p[@class='s2 strong']")

    # To list
    schedule_list = (subject.text for subject in schedule_elements)

    # Delete old data
    old_data = session.query(Schedule).filter(Schedule.weekday == week_day).delete()

    # Create new data
    for subject in schedule_list:
        schedule = Schedule(name=subject, weekday=week_day)
        session.add(schedule)
        session.commit()

    # to close the browser
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
