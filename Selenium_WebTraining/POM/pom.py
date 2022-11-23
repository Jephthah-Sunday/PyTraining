import time
from contactPage import ContactPage
from aboutUs import AboutUsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    about_page = AboutUsPage(driver)
    print(about_page.title.text)
    contact_page = ContactPage(driver)
    print(contact_page.firstname_input, contact_page.lastname_input)
    contact_page.submit_button.click()
    time.sleep(20)


if __name__ == '__main__':
    main()