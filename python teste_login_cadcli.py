from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver
driver = webdriver.Chrome()

try:
    # 1. Acessar a página de login
    driver.get("http://localhost/pdv")  # URL local fornecida no HTML

    # 2. Preencher os campos do formulário de login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputEmail"))
    )
    email_input = driver.find_element(By.ID, "inputEmail")
    senha_input = driver.find_element(By.ID, "inputPassword")

    # Inserir e-mail e senha
    email_input.send_keys("teste@exemplo.com")  # Insira um e-mail válido aqui
    senha_input.send_keys("123456")  # Insira uma senha válida aqui

    # 3. Submeter o formulário de login
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # 4. Validar redirecionamento ou mensagem de erro
    WebDriverWait(driver, 10).until(
        EC.url_contains("home")
    )
    print("Login bem-sucedido! Página redirecionada.")

    # 5. Acessar a página de cadastro de cliente
    driver.get("http://localhost/pdv/cliente")

    # 6. Preencher os campos do formulário de cliente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nome"))
    )
    driver.find_element(By.ID, "nome").send_keys("João Silva")
    driver.find_element(By.ID, "email").send_keys("joao.silva@example.com")
    driver.find_element(By.ID, "cpf").send_keys("123.456.789-00")
    driver.find_element(By.ID, "telefone").send_keys("(11) 98765-4321")
    driver.find_element(By.ID, "cep").send_keys("01001-000")
    driver.find_element(By.ID, "rua").send_keys("Rua Exemplo")
    driver.find_element(By.ID, "bairro").send_keys("Bairro Exemplo")
    driver.find_element(By.ID, "cidade").send_keys("São Paulo")
    driver.find_element(By.ID, "estado").send_keys("SP")
    driver.find_element(By.ID, "numero").send_keys("123")

    # 7. Submeter o formulário de cliente
    driver.find_element(By.ID, "submit").click()

    # 8. Validar mensagem de sucesso ou erro
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "alert"))
    )
    alert_message = driver.find_element(By.ID, "alert").text
    if "sucesso" in alert_message.lower():
        print("Cliente cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar cliente: {alert_message}")

finally:
    # Fechar o navegador
    driver.quit()
