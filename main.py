import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from selenium import webdriver

active_threads = 0
lock = Lock()

def run_test():
    global active_threads
    try:
        grid_url = "http://192.168.68.217:4444"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options,
        )
        driver.get("https://www.google.com")
        print(driver.title)
        random_sleep = random.randint(5, 25)
        print(f"Sleeping for {random_sleep} seconds")
        time.sleep(random_sleep)
    finally:
        driver.quit()
        print("Driver closed")

if __name__ == "__main__":
    n = 25
    with ThreadPoolExecutor(max_workers=n) as executor:
        futures = []
        with lock:
            active_threads = n
        for _ in range(n):
            futures.append(executor.submit(run_test))
        for future in as_completed(futures):
            with lock:
                active_threads -= 1
                print(f"Threads still running: {active_threads}")