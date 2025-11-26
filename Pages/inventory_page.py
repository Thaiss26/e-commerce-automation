from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.botoes_adicionar = (By.CSS_SELECTOR, '.btn_primary.btn_inventory')
        self.link_carrinho = (By.CSS_SELECTOR, 'a.shopping_cart_link')

    def adicionar_todos_produtos(self):
        print("Adicionando todos os produtos ao carrinho...")

        count = 0
        while True:
            botoes = self.encontrar_elementos(self.botoes_adicionar)

            if not botoes:
                break

            botoes[0].click()
            count += 1
        
        print(f"{count} produto(s) adicionado(s) ao carrinho!")

    def acessar_carrinho(self):
        print("Acessando o carrinho de compras...")
        self.clicar(self.link_carrinho)
        self.esperar_elemento((By.CSS_SELECTOR, '.cart_item'))
