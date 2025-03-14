import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obter o diretório atual do script
download_dir = os.path.abspath(os.path.dirname(__file__))

# Configurar opções do Firefox
options = Options()
options.add_argument("--headless")  # Ativar headless
options.add_argument("--disable-gpu")  # Evita problemas gráficos no headless
options.add_argument("--no-sandbox")  # Segurança para modo headless
options.add_argument("--disable-blink-features=AutomationControlled")  # Evita bloqueios de bot
options.set_preference("dom.webdriver.enabled", False)  # Tenta evitar detecção de bot
options.set_preference("useAutomationExtension", False)  # Remove flag de automação
options.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
)  # Emula um navegador real

# Configurações de download
options.set_preference("browser.download.folderList", 2)  # 2 = Diretório personalizado
options.set_preference("browser.download.manager.showWhenStarting", False)  # Não mostrar janela de download
options.set_preference("browser.download.dir", download_dir)  # Define o diretório do script como destino
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel,application/pdf,text/plain")  # Download automático


navegador = webdriver.Firefox(options=options)


link = ""
navegador.get(url=link)


try:
    inputUsuario = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "txtlogin"))
    )
    inputUsuario.send_keys("")
except:
    print("Elemento 'txtlogin' não encontrado após o redirecionamento.")

inputSenha = navegador.find_element(by=By.ID, value="txtSurvey")
inputSenha.send_keys("")

buttonLogin = navegador.find_element(by=By.ID, value="Button1")
buttonLogin.click()
sleep(4)

wait = WebDriverWait(navegador, 10)


wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "pace-active")))


export_btn = wait.until(EC.element_to_be_clickable((By.ID, "exportBtn")))
export_btn.click()

frameFiltros = navegador.find_element(by=By.NAME, value="m_oWdw")
navegador.switch_to.frame(frameFiltros)

baixar = wait.until(EC.element_to_be_clickable((By.ID, "m_m_oBtnOk")))
baixar.click()


def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime) 
    return latest_file


print("Aguardando o download...")
sleep(5)  
downloaded_file = get_latest_file(download_dir)

if downloaded_file:
    print(f"Arquivo baixado: {downloaded_file}")
    
    
    file_extension = os.path.splitext(downloaded_file)[1]  # Pega a extensão do arquivo (ex.: .csv, .pdf)
    new_file_name = os.path.join(download_dir, f"base{file_extension}")  # Novo nome: "base" + extensão
    

    os.rename(downloaded_file, new_file_name)  # Renomeia o arquivo
    print(f"Arquivo renomeado para: {new_file_name}")
else:
    print("Nenhum arquivo foi detectado no diretório após o download.")
    new_file_name = None

# Fechar o navegador
navegador.quit()

# Chamar o script tratarDados.py com o arquivo renomeado
if new_file_name:
    try:
        # Executa o script tratarDados.py passando o caminho do arquivo renomeado como argumento
        subprocess.run(["python", "tratarDados.py", new_file_name], check=True)
        print("Script tratarDados.py executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar tratarDados.py: {e}")
else:
    print("Não foi possível executar tratarDados.py porque o arquivo não foi encontrado.")