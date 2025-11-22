from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def create_driver():
    # Caminho correto do executável do ChromeDriver
    driver_path = ChromeDriverManager().install()

    # Se a string não terminar com .exe, tentamos achar o executável correto
    if not driver_path.endswith(".exe"):
        folder = os.path.dirname(driver_path)
        for file in os.listdir(folder):
            if file.startswith("chromedriver") and file.endswith(".exe"):
                driver_path = os.path.join(folder, file)
                break

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

