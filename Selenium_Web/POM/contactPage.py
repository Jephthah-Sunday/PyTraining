from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/contact")
        self.email_input = driver.find_element(By.NAME, 'email')
        self.firstname_input = driver.find_element(By.NAME, 'firstname')
        self.lastname_input = driver.find_element(By.NAME, 'lastname')
        self.message_textarea = driver.find_element(By.NAME, 'message')
        self.submit_button = driver.find_element(By.TAG_NAME, 'button')