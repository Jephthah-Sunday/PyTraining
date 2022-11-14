import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    email_inputs = driver.find_elements(By.NAME, "email")
    print("Found ", len(email_inputs), " email input")

    # Forms
    forms = driver.find_elements(By.TAG_NAME, "form")
    print("Found ", len(forms), " form")

    first_form = forms[0]
    contact_us_form_email_inputs = first_form.find_elements(By.NAME, "email")
    print("First form Found ", len(contact_us_form_email_inputs), " email input")




if __name__ == '__main__':
    main()