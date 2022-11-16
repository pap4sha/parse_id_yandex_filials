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

        while True:
            find_more_element = driver.find_element("div", "add-business-view")

            if driver.find_elements("div", "scroll__container"):
                with open("test.html", "w") as file:
                    file.write(driver.page_source)

                    break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_more_element).perform()
                time.sleep(3)
    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()


get_sourse_html(url = 'https://yandex.ru/maps/?display-text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&ll=50.417027%2C55.287521&mode=search&page=3&sctx=ZAAAAAgBEAAaKAoSCVmis8wixklAEVK4HoXrPUtAEhIJYOemzTgNkT8RbsST3cyIHUAiBgABAgMEBSgKOABA71ZIAWIRb2JqZWN0c19kaXNhYmxlPTFqAnJ1nQHNzEw9oAEAqAEAvQGi8zndwgGCAdazkMqjBb7X3dMEg%2FCYhQTZ0%2F%2BIBKnl8%2BSNBZXT9cMEusLLngSl9cvABImEooUE0s%2FbqgTet5zeBqKNtYMEl%2FLZygTip6fzBIz7gceUA%2FDVjrYE6%2FTfzATS9oXY1QHWo6KtBNPw9r4E3M2LrATzgpieBMLToq4ErqiHu2baqOatjAPqAQDyAQD4AQCCAhTRgtCw0YLRgtC10LvQtdC60L7QvIoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=50.417027%2C55.287521&sspn=8.081710%2C4.154782&text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&z=7.2')