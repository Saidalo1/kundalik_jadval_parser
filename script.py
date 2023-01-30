import logging
import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

from models import session, Schedule, ErrorSchedule
from config import week_day, year, month, day

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

    # Save current url to old_current_url
    old_current_url = driver.current_url

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

    # get current url
    current_url = driver.current_url

    if current_url == 'https://kundalik.com/billing/paidAccess/paymentPage':
        # Delete old errors
        session.query(ErrorSchedule).filter(ErrorSchedule.weekday == week_day).delete()

        # get domain name
        current_domain_name = urlparse(current_url).netloc

        # error message
        error_message = f"{LOGIN} accounti uchun {current_domain_name} saytida to'lov amalga oshirilmagan!"

        # save error message to ErrorSchedule table with today's weekday
        error_schedule = ErrorSchedule(error_text=error_message, weekday=week_day)
        session.add(error_schedule)
        session.commit()

        # exit from function
        return
    elif current_url == old_current_url:
        # Delete old errors
        session.query(ErrorSchedule).filter(ErrorSchedule.weekday == week_day).delete()

        # error message
        error_message = "Login yoki password xato!"

        # save error message to ErrorSchedule table with today's weekday
        error_schedule = ErrorSchedule(error_text=error_message, weekday=week_day)
        session.add(error_schedule)
        session.commit()

        # exit from function
        return

    # Login to timetable url
    driver.get(f'https://kundalik.com/user/calendar.aspx?year={year}&month={month}&day={day}')

    # Find lesson schedule for today
    schedule_elements = driver.find_elements(By.XPATH, "//p[@class='s2 strong']")

    # To list
    schedule_list = [subject.text for subject in schedule_elements]

    # Delete old data
    session.query(Schedule).filter(Schedule.weekday == week_day).delete()

    # Create new data
    if len(schedule_list) > 0:
        for subject in schedule_list:
            schedule = Schedule(name=subject, weekday=week_day)
            session.add(schedule)
            session.commit()
    else:
        # Delete old errors
        session.query(ErrorSchedule).filter(ErrorSchedule.weekday == week_day).delete()

        # Add error
        schedule = ErrorSchedule(error_text='Dars jadvali topilmadi', weekday=week_day)
        session.add(schedule)
        session.commit()

    # to close the browser
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
