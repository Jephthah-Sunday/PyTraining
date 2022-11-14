import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def print_element_attributes(element):
    print("\nID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("innerText"))
    print("Inner HTML:", element.get_attribute("innerHTML"))



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    print_element_attributes(academy_link)
    form = driver.find_element(By.TAG_NAME, "form")
    print_element_attributes(form)





if __name__ == '__main__':
    main()