from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self):
        super().__init__()  # inicializa BasePage e cria o driver

        # Elementos
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (
            By.XPATH,
            "//*[@data-test='inventory-item-name' and text()='{}']"
        )
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.encontrar_elemento(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item_formatado = (
            self.item_inventario[0],
            self.item_inventario[1].format(nome_item)
        )
        self.clicar(item_formatado)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

