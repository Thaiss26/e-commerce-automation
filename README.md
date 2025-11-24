
# E-commerce Automation com Python + Selenium + Pytest

Este repositório contém conjunto de testes automatizados com Selenium e Pytest, simulando o fluxo completo de compra em uma aplicação web. O projeto inclui cenários funcionais e estrutura modelar baseada em Page Objects.


# Tecnologias Utilizadas

* Python 3.13.3
*  Pytest
*  Selenium
* Estrutura Page Object Model (POM) 


# Cenários de testes

* ✅Login no Sistema
* ✅ Adição de todos os produtos ao carrinho
* ✅ Prenchendo os dados do checkout
* ✅ Finalização da compra 
* ✅ Logout do Sistema


# Instalação e Execução

# Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

# Instale as dependências
```bash
pip install -r requirements.txt
```

# Instale o Selenium Webdriver
```bash
selenium install
```

# Rode os Testes
```bash
pytest Testes/test_compra.py
```



