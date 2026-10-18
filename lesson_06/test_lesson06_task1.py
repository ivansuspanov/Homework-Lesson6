from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div#start button"))
        )
        start_button.click()

        hello_text_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        driver.save_screenshot(
            "dynamic_loading_result.png")

        assert hello_text_element.text == "Hello World!", (
             "Текст не совпадает с ожидаемым"
        )

    finally:
        driver.quit()
