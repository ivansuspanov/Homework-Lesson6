from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


USER1_COOKIE = {
    "name": "session_id",
    "value": "NWQzNGUzYTEtZGJlZC00MWMwLTlkNzItNTYwNGY4ZWRjY2Ex",
    "domain": ".gitflic.ru",
    "path": "/",
}

USER2_COOKIE = {
    "name": "session_id",
    "value": "NWYzMmMyYWQtYmIwZi00NThmLTg0MTUtZTczYWUzZmNjMzM0",
    "domain": ".gitflic.ru",
    "path": "/",
}

USER1_PROFILE_URL = "https://gitflic.ru/user/shushpanovivan"
USER2_PROFILE_URL = "https://gitflic.ru/user/yekaterina"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://gitflic.ru/")

        driver.delete_all_cookies()
        driver.add_cookie(USER1_COOKIE)
        driver.refresh()

        wait.until(lambda d: d.current_url != "about:blank")
        wait.until(lambda d: d.find_element("tag name", "body"))

        driver.get(USER1_PROFILE_URL)
        wait.until(lambda d: USER1_PROFILE_URL in d.current_url)

        url_after_user1 = driver.current_url
        print(f"User1 URL: {url_after_user1}")

        driver.delete_all_cookies()
        driver.add_cookie(USER2_COOKIE)
        driver.refresh()

        wait.until(lambda d: d.current_url != "about:blank")
        wait.until(lambda d: d.find_element("tag name", "body"))

        driver.get(USER2_PROFILE_URL)
        wait.until(lambda d: USER2_PROFILE_URL in d.current_url)

        url_after_user2 = driver.current_url
        print(f"User2 URL: {url_after_user2}")

        assert url_after_user1 != url_after_user2, (
            f"URL профилей не различаются! "
            f"User1: {url_after_user1}, "
            f"User2: {url_after_user2}"
        )
        print("Тест пройден: URL отличаются.")

    except Exception as e:
        print(f"Ошибка теста: {e}")
        raise e
    finally:
        driver.quit()
