import time

from selenium import webdriver

try:
    grid_url = "http://192.168.68.217:4444"
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options,
    )
    driver.get("https://www.google.com")
    print(driver.title)

    time.sleep(120)
finally:
    driver.quit()
    print("Driver closed")
