import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def send_keys_to_element(element, *keys):
    element.send_keys(keys)




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    send_keys_to_element(driver.find_element(By.XPATH, '//*[@id="email"]'), "Jephthah@testify.com")
    send_keys_to_element(driver.find_element(By.XPATH, '//*[@id="pass"]'), "Jephthahtestar")
    form = driver.find_element(By.TAG_NAME, 'form')
    login_button = form.find_element(By.TAG_NAME, 'button')
    login_button.click()
    time.sleep(20)







if __name__ == '__main__':
    main()