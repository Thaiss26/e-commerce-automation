from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.botao_checkout = (By.XPATH, "//button[@data-test='checkout']")
    
    def iniciar_checkout(self):
        print("Iniciando processo de checkout...")
        self.clicar(self.botao_checkout)
