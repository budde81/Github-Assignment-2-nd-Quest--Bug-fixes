import sys
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main() -> int:
    search_query = "Python Selenium"
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.google.com")

        search_box = wait.until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(search_query)
        search_box.submit()

        wait.until(
            lambda _: urlparse(driver.current_url).path in {
                "/search",
                "/sorry/index",
            }
        )
        if urlparse(driver.current_url).path == "/sorry/index":
            print(
                "Google requires verification. Complete it manually in the "
                "browser window."
            )
            input("After verification, press Enter here to continue...")

        results_wait = WebDriverWait(driver, 120)
        results_wait.until(
            lambda _: urlparse(driver.current_url).path == "/search"
        )
        results_wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        print(driver.title)
        return 0
    except InvalidSessionIdException:
        print(
            "The Chrome WebDriver session ended because the browser window "
            "closed or disconnected. Keep the Chrome window open while "
            "completing verification, then run the script again.",
            file=sys.stderr,
        )
        return 1
    finally:
        try:
            driver.quit()
        except InvalidSessionIdException:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
