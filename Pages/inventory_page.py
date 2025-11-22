from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.botoes_adicionar = (By.CSS_SELECTOR, '.btn_primary.btn_inventory')
        self.link_carrinho = (By.CSS_SELECTOR, 'a.shopping_cart_link')

    def adicionar_todos_produtos(self):
        print("Adicionando todos os produtos ao carrinho")
        botoes = self.encontrar_elementos(self.botoes_adicionar)
        count = len(botoes)

        for botao in botoes:
            botao.click()


        print(F"{count} produtos(s) adicionado(s) ao carrinho!")

    def acessar_carrinho(self):
        print("Acessando o carrinho de compras...")
        self.clicar(self.link_carrinho)


    # espera um item aparecer no carrinho
        self.esperar_elemento((By.CSS_SELECTOR, '.cart_item'))
    


