import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_login_page_loads():
    options = Options()
    options.add_argument("--headless")   # Important for QATouch cloud run
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://opensource-demo.orangehrmlive.com/")

    title = driver.title
    print("Page Title is:", title)

    assert "OrangeHRM" in title, "Login Page Failed"

    driver.quit()
