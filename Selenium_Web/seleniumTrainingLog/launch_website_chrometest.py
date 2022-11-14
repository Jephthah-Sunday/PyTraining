import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get("https://facebook.com")
    driver.get("https://www.testifyltd.com/contact")
    #locate_by_id(driver)
    #locate_by_name(driver)
    #locate_by_class_name(driver)
    #locate_by_tag_name(driver)
    #locate_by_css_selector(driver)
    #locate_by_XPATH(driver)
    #locate_by_link_text(driver)
    locate_by_partial_link_text(driver)
    #hero_element = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div[1]/div[1]/h1")
    #print("Hero Element", hero_element, hero_element.text)
    #links = driver.find_elements(By.TAG_NAME, "a")
    #for link in links:
    #    print("Link:", link.text)


def locate_by_name(driver):
    first_element = driver.find_element(By.NAME, 'firstname')
    print("Email Element", first_element)
    lastname_element = driver.find_element(By.NAME, 'lastname')
    print("Password Element", lastname_element)


def locate_by_id(driver):
    pass



def locate_by_class_name(driver):
        rr_first_element = driver.find_element(By.CLASS_NAME, 'react-reveal')
        print("React Reveal First Element", rr_first_element)
        rr_first_elements = driver.find_elements(By.CLASS_NAME, 'react-reveal')
        for rr_first_element in rr_first_elements:
            print("React Reveal First Element", rr_first_element)


def locate_by_tag_name(driver):
    first_input = driver.find_element(By.TAG_NAME, "input")
    print("First Input Element:", first_input)
    div_elements = driver.find_elements(By.TAG_NAME, "div")
    print("Total Divs:", len(div_elements))
    for div_element in div_elements:
        print("Div Element:", div_element)


def locate_by_css_selector(driver):
    firstname_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > form > div:nth-child(1) > div:nth-child(1) > input")
    print("Firstname Element By CSS Selector:", firstname_element)
    input_elements = driver.find_elements(By.CSS_SELECTOR, "div")
    print("Total div.relative:", len(input_elements))
    for input_element in input_elements:
        print("Div Element:", input_element)



def locate_by_XPATH(driver):
    form = driver.find_element(By.XPATH, "//form[1]")
    print("Form:", form)
    form_by_full_xpath = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[1]/div[1]/input')
    print("Form By Full Xpath:", form_by_full_xpath)



def locate_by_link_text(driver):
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    print("Academy link:", academy_link)
    hire_link = driver.find_element(By.LINK_TEXT, 'Hire')
    print("Hire Link:", hire_link)
    

def locate_by_partial_link_text(driver):
    academy_link = driver.find_element(By.PARTIAL_LINK_TEXT, "adem")
    print("Academy link:", academy_link)
    tests_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Test")
    print("Test Links size:", len(tests_links))
    for tests_links in tests_links:
        print("A Test link:", tests_links)



if __name__ == '__main__':
    main()