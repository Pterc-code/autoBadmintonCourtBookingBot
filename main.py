import schedule
import time
from datetime import datetime
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver


def LogIn(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="loginLink"]').click()
    time.sleep(1)
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="section-sign-in-first"]/div[6]/div/button')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(
        username)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(
        password)
    driver.find_element(By.NAME, '_eventId_proceed').click()


def searchBadminton(driver):
    """
    Search for badminton in the search bar
    """
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'term')))
    search_bar.send_keys('badminton')
    search_bar.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                '//*[@id="list-group"]/a[4]/div/div[2]/div[1]/p'))).click()  # AC


def book(session, driver):
    session.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="btnAccept"]')
    driver.execute_script("arguments[0].click();", button)

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="mainContent"]/div[2]/form[2]/div[2]/button[2]'))).click()

    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="checkoutButton"]')
    driver.execute_script("arguments[0].click();", button)

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="CheckoutModal"]/div/div/div[2]/button[2]'))).click()


def searchSession(driver):
    sessions = driver.find_elements(By.CLASS_NAME, "card-body")

    start = datetime.time(12, 30, 0)
    end = datetime.time(17, 30, 0)
    format = '%I:%M%p'

    for session in sessions:
        session_time = session.text.split(" ")[3].split("\n")[1] + \
                       session.text.split(" ")[4]
        current = datetime.datetime.strptime(session_time, format).time()
        if start <= current <= end:
            if "REGISTER" in session.text:
                book(session, driver)
                break


def bookAfternoon(driver, userName, Password):
    LogIn(driver, userName, Password)
    searchBadminton(driver)
    searchSession(driver)
    driver.close()


if __name__ == "__main__":
    userName = input('Enter your username: ')
    password = input('Enter your password: ')


    def main():
        driver = webdriver.Chrome()
        driver.get("https://recreation.utoronto.ca/")
        driver.maximize_window()
        bookAfternoon(driver, userName, password)


    schedule.every().day.at("12:59:55").do(main)
    schedule.every().day.at("13:59:55").do(main)
    schedule.every().day.at("14:59:55").do(main)
    schedule.every().day.at("15:59:55").do(main)
    schedule.every().day.at("16:59:55").do(main)
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)
