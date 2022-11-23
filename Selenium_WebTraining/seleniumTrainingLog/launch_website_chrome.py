import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    #driver = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\TEST AUTOMATION SCHOOL\Webdrivers\chromedriver_win32\chromedriver.exe" )
    #chromedriver_autoinstaller.install()
    #driver = webdriver.Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.google.com")
    driver.close()




if __name__ == '__main__':
    main()