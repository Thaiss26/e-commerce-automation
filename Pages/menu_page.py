from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
        self.titulo_pagina = (By.XPATH, "//span[contains(@class, 'title')]")
        self.item_inventario = (By.XPATH, "//div[@data-test='inventory-item-name' and contains(text(), '{}')]")
        self.botao_adicionar = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.icone_carrinho = (By.XPATH, "//a[contains(@class, 'shopping_cart_link')]")
        self.botao_menu = (By.XPATH, "//button[contains(@id, 'react-burger-menu-btn')]")
        self.botao_logout = (By.XPATH, "//a[contains(@id, 'logout_sidebar_link')]")

    def verificar_login_com_sucesso(self):
        self.encontrar_elemento(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item_formatado = (
            self.item_inventario[0],
            self.item_inventario[1].format(nome_item)
        )

        # Clica no item específico
        self.clicar(item_formatado)

        self.clicar(self.botao_adicionar)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

    def logout(self):
        print("Realizando logout...")

        self.clicar(self.botao_menu)

        # Aguarda o botão estar clicável
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(self.botao_logout))

        # Clica no logout
        self.clicar(self.botao_logout)
