import pytest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.menu_page import MenuPage


@pytest.mark.feature("Fluxo de compra")
def test_fluxo_de_compra(setup_teardown):
    """
    Teste automatizado que valida o fluxo de compra completo com sucesso no sistema.
    - Login
    - Adição de produtos
    - Checkout
    - Logout
    """

    driver = setup_teardown 

    # Instanciando as páginas com o driver vindo do conftest
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    menu = MenuPage(driver)

    # Login no sistema
    login.acessar()
    login.preencher_dados()
    login.logar()
    menu.verificar_login_com_sucesso()

    # Adcionando todos os produtos ao carrinho
    inventory.adicionar_todos_produtos()
    inventory.acessar_carrinho()

    # Iniciando o checkout
    cart.iniciar_checkout()

    # Preenchendo as informações no checkout
    checkout.preencher_info()
    checkout.continuar_e_finalizar()

    # LOGOUT
    menu.logout()

    print("Teste finalizado com sucesso!")