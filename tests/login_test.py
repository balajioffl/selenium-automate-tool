# TA-10: Verify Login Page Loads

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")

print("Page Title is:", driver.title)

if "OrangeHRM" in driver.title:
    print("Login Page Loaded - PASS")
else:
    print("Login Page Failed - FAIL")

driver.quit()
