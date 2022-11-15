from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# option = Options()
# option.add_argument("--disable-infobars")
browser = webdriver.Chrome(executable_path='C:/Users/tat100zmi/PycharmProjects/chrome_webdriver/chromedriver.exe')
def parse():
    try:
        driver = browser.get(url = 'https://yandex.ru/maps/?display-text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&ll=50.417027%2C55.287521&mode=search&page=3&sctx=ZAAAAAgBEAAaKAoSCVmis8wixklAEVK4HoXrPUtAEhIJYOemzTgNkT8RbsST3cyIHUAiBgABAgMEBSgKOABA71ZIAWIRb2JqZWN0c19kaXNhYmxlPTFqAnJ1nQHNzEw9oAEAqAEAvQGi8zndwgGCAdazkMqjBb7X3dMEg%2FCYhQTZ0%2F%2BIBKnl8%2BSNBZXT9cMEusLLngSl9cvABImEooUE0s%2FbqgTet5zeBqKNtYMEl%2FLZygTip6fzBIz7gceUA%2FDVjrYE6%2FTfzATS9oXY1QHWo6KtBNPw9r4E3M2LrATzgpieBMLToq4ErqiHu2baqOatjAPqAQDyAQD4AQCCAhTRgtCw0YLRgtC10LvQtdC60L7QvIoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=50.417027%2C55.287521&sspn=8.081710%2C4.154782&text=%D1%82%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&z=7.2')

    except Exception as ex:
        print(ex)
    while True:
        driver.execute_script("window.scroll(0, 1080)")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # finally:
        # browser.close()
        # browser.quit()

if __name__ == "__main__":
    parse()