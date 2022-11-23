import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, 'form')
    print("Form Status:", form.is_displayed(), form.is_enabled())
    submit_button = form.find_element(By.TAG_NAME, 'button')
    driver.maximize_window()
    print("Submit Button Status:", submit_button.is_displayed(), submit_button.is_enabled())
    time.sleep(20)







if __name__ == '__main__':
    main()