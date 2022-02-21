import schedule
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.utoronto.ca/utogether/ucheck")
driver.maximize_window()


def LoggingIn():
    """
    Log into recreation.utoronto.ca
    """
    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="block-system-main"]/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/a')
    driver.execute_script("arguments[0].click();", button)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(
        '')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(
        '')
    driver.find_element(By.NAME, '_eventId_proceed').click()


def fill_out_questions():

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/button/span[1]'))).click()

    # Do any of the following statements apply to you?
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="f5d87fa4-41c1-41bf-9307-2eb2e7862a28-noFocus"]/fieldset/label[2]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # Are you currently experiencing any of these symptoms?
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ebdd2acd-87ff-47aa-a7d2-059677987580-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # Is anyone you live with currently experiencing any new COVID-19 symptoms and/or waiting for test results after experiencing symptoms?
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # In the last 14 days, have you travelled outside of Canada and been told to quarantine
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="296a215c-8f44-4ca0-b2bc-6861ddabec3b-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # Has a doctor, health care provider, or public health unit told you that you should currently be isolating (staying at home)?
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2a1ba3f-0113-49a6-95cc-aeede171963a-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # In the last 10 days, has someone in your household experienced any COVID-19 symptoms and/or tested positive for COVID-19 (on a rapid antigen test or PCR test)?
    element = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//*[@id="5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # In the last 14 days, have you received a COVID Alert exposure notification on your cell phone?
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="156f6b12-1f8a-491c-9261-2dd73aef9d6a-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # In the last 10 days, have you been identified as a "close contact" of someone who currently has COVID-19 (confirmed by a PCR or rapid antigen test)?
    element = WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="11985099-8548-4dc6-944f-bb4ea9c9494b-noFocus"]/fieldset/label[1]')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

    # submit
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/main/div/div/div/div/div/button')))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)


if __name__ == "__main__":

    def ucheck():
        LoggingIn()
        fill_out_questions()

    schedule.every().day.at("08:00:00").do(ucheck)

    ucheck()
    while True:
        schedule.run_pending()
        time.sleep(1)
