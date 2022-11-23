import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC




def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()

def sweet_test(driver):
    driver.get("https://www.youtube.com/watch?v=VGecJY7u6So")
    action = ActionChains(driver)
    driver.maximize_window()
    #time.sleep(60)
    scroll_by_offset(action, 450)
    web_driver_wait = WebDriverWait(driver, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "ytd-comment-renderer")))

    comments = driver.find_elements(By.TAG_NAME, 'ytd-comment-renderer')
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)

def main():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    sweet_test(chrome_driver)
    time.sleep(20)
    #driver.get("https://m.youtube.com/watch?v=rmSEfgRWkcQ")
    #comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/ytm-watch/ytm-single-column-watch-next-results-renderer/div/ytm-item-section-renderer[1]/lazy-list/ytm-comments-entry-point-header-renderer')
    #comment.click()
    #time.sleep(20)
    #comment_modal = driver.find_element(By.XPATH, '//*[@id="app"]/panel-container/ytm-engagement-panel/ytm-engagement-panel-section-list-renderer/div/div/div[2]/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/ytm-comments-header-renderer/ytm-comment-simplebox-renderer')
    #time.sleep(comment_modal.is_displayed())
    #Comment_1 = driver.find_element(By.XPATH, '//*[@id="main"]')
    #print("This is the First Comment:", Comment_1.text)
    #Comment_2 = driver.find_element(By.XPATH, '//*[@id="app"]/panel-container/ytm-engagement-panel/ytm-engagement-panel-section-list-renderer/div/div/div[2]/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-comment-thread-renderer[2]/ytm-comment-renderer')
    #print("This is the Second Comment:", Comment_2.text)





if __name__ == '__main__':
    main()

