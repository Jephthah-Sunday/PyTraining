import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.testifyltd.com/contact")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(15)







if __name__ == '__main__':
    main()