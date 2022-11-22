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
            # find_more_element = driver.find_element(By.CLASS_NAME, "scroll__scrollbar-thumb")
            # start = find_more_element.location
            # print (find_more_element)

            if driver.find_elements(By.CLASS_NAME, "add-business-view"):
                with open("test.html", "w", encoding = "utf-8") as file:
                    file.write(driver.page_source)

                break
            else:
                find_more_element = driver.find_element(By.CLASS_NAME, "scroll__scrollbar-thumb")
                try:
                    actions = ActionChains(driver)
                    actions.drag_and_drop_by_offset(find_more_element, 0, 100).perform()
                    time.sleep(3)
                except Exception as ex:
                    print (ex)
    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()


get_sourse_html(url = 'https://yandex.ru/maps/?display-text=%D0%A2%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC&ll=50.277429%2C55.501128&mode=search&page=3&sctx=ZAAAAAgBEAAaKAoSCTzbozfcB0lAEabydoTTnktAEhIJF7zoK0jLIkAR%2BmLvxRftCUAiBgABAgMEBSgKOABA71ZIAWoCcnWdAc3MTD2gAQCoAQC9AZ6LVPjCAYcBvtfd0wT5z4OH%2BAbd8c2VkwGf0qrw5ALKjf%2FeA963nN4Goo21gwTKyqHuA9azkMqjBfGJ5MuuAanl8%2BSNBYmEooUE0vaF2NUBuuyq7c8G86q2pwTSz9uqBLDQvajvBZqltLwE0eWF3zCh2r2ZBev038wEzsKlhwXczYusBIeIiYQE2uqbwPcD6gEA8gEA%2BAEAggIaKChjaGFpbl9pZDooMTUwOTA0NTUzMDQpKSmKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=50.277429%2C55.501128&sspn=6.199731%2C2.123854&text=%7B%22text%22%3A%22%D0%A2%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%2215090455304%22%5D%7D%5D%7D&z=8.16')
