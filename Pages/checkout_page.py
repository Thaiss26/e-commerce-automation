from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
        self.input_nome = (By.XPATH, "//input[@data-test='firstName']")
        self.input_sobrenome = (By.XPATH, "//input[@data-test='lastName']")
        self.input_cep = (By.XPATH, "//input[@data-test='postalCode']")
        self.botao_continuar = (By.XPATH, "//input[@data-test='continue']")
        self.botao_finalizar = (By.XPATH, "//button[@data-test='finish']")
        self.resumo_info = (By.XPATH, "//*[@class='summary_info']")
        self.cabecalho_finalizado = (By.XPATH, "//*[@class='complete-header']")


    def preencher_info(self):
        print("Preenchendo informações do checkout...")
        self.escrever(self.input_nome, "Thais")
        self.escrever(self.input_sobrenome, "Silva")
        self.escrever(self.input_cep, "91130-770")

    def continuar_e_finalizar(self):
        print("Continuando e finalizando compra...")

        self.clicar(self.botao_continuar)
        self.esperar_elemento(self.resumo_info)

        self.clicar(self.botao_finalizar)
        self.esperar_elemento(self.cabecalho_finalizado)

        print("Compra finalizada com sucesso!")
