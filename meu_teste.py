from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho do chromedriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Abre a página de cadastro
driver.get("https://kathon.tech/CadastroEstudante")
driver.maximize_window()  # Maximiza a tela para evitar erros de visibilidade

try:
    wait = WebDriverWait(driver, 10)

    # Preenche o campo "Nome"
    nome_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    nome_input.send_keys("Paulo Henrique")

    # Preenche o campo "Email"
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
    email_input.send_keys("paulo@exemplo.com")

    # Faz o upload da foto de perfil
    foto_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    foto_input.send_keys("C:\\Users\\phnal\Pictures\\eu_perfil_2.jpeg")  

    # Preenche o campo "CPF"
    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text'][not(@type='date')]")))
    cpf_input.send_keys("123.456.789-00")  # Exemplo

    # Preenche a "Data de nascimento"
    nascimento_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='date']")))
    nascimento_input.send_keys("2000-01-01")  # Formato: YYYY-MM-DD

    # Preenche o campo "Celular"
    celular_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text'][@placeholder='']")))
    celular_input.send_keys("11999999999")

    # Preenche o campo "Senha"
    senha_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
    senha_input.send_keys("senha123")

    # Clica no botão "Cadastrar Jovem"
    cadastrar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cadastrar Jovem')]")))
    cadastrar_button.click()

    # Aguarda alguns segundos para o processamento
    time.sleep(5)
    print("Cadastro realizado com sucesso!")

except Exception as e:
    print(f"Erro ao preencher o formulário: {e}")

# Fecha o navegador
driver.quit()
