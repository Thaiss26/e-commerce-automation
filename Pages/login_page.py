from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from utils.config import URL, USUARIO, SENHA



class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = URL

    def acessar(self):
        print("Acessar a página de login...")
        self.driver.get(self.url)
    
    def preencher_dados(self, usuario=USUARIO, senha=SENHA):
        print("Preenchendo dados de login...")
        self.escrever(self.USERNAME, usuario)
        self.escrever(self.PASSWORD, senha)
        
    def logar(self):
        print("Efetuando login...")
        self.clicar(self.LOGIN_BTN)
        print("Login realizado com sucesso!")
