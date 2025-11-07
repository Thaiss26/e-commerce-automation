from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)  # aqui também faltava passar o service
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
