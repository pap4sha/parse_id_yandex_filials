from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import requests


def get_sourse_html(url):

    driver = webdriver.Chrome(executable_path='C:/Users/tat100zmi/PycharmProjects/chrome_webdriver/chromedriver.exe')

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        # while True:
        try:
            driver.find_element(By.CLASS_NAME, "input__control._bold").send_keys('Таттелеком')
        except Exception as ex:
            print (ex)

        try:
            search_button = driver.find_element(By.CLASS_NAME, 'small-search-form-view__button')
            zoom_out = driver.find_element(By.CLASS_NAME, 'zoom-control__zoom-out')
            actions = ActionChains(driver)
            actions.click(search_button).perform()
            time.sleep(1)
            actions.click(zoom_out).perform()
            time.sleep(1)
            actions.click(zoom_out).perform()
            time.sleep(1)
            actions.click(zoom_out).perform()
        except Exception as ex:
            print (ex)
        time.sleep(5)

        while True:
            if driver.find_elements(By.CLASS_NAME, "add-business-view"):
                find_more_element = driver.find_element(By.CLASS_NAME, "scroll__scrollbar-thumb")
                actions2 = ActionChains(driver)
                actions2.drag_and_drop_by_offset(find_more_element, 0, 100).perform()
                time.sleep(3)
                actions2.drag_and_drop_by_offset(find_more_element, 0, 100).perform()
                time.sleep(3)
                actions2.drag_and_drop_by_offset(find_more_element, 0, 100).perform()
                time.sleep(3)
                with open("test.html", "w", encoding = "utf-8") as file:
                    file.write(driver.page_source)

                break
            else:
                find_more_element = driver.find_element(By.CLASS_NAME, "scroll__scrollbar-thumb")
                try:
                    actions2 = ActionChains(driver)
                    actions2.drag_and_drop_by_offset(find_more_element, 0, 100).perform()
                    time.sleep(3)
                except Exception as ex:
                    print (ex)
    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()


# get_sourse_html(url = 'https://yandex.ru/maps/?ll=52.583698%2C56.067155&z=5.86')
