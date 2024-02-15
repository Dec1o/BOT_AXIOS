from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pyautogui
import pyperclip

def realizar_chamada():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)

    # Entrar no Directcall:
    time.sleep(5)
    navegador.get("https://gestor.directcallsoft.com/usuarios")

    # Fazer login no Directcall
    time.sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="emaillogin"]').send_keys("")
    navegador.find_element(By.XPATH, '//*[@id="test"]/div[2]/div/input').send_keys("")
    time.sleep(1)
    pyautogui.click()

    # Clicar no discador e discar número:
    time.sleep(20)
    pyautogui.click()
    time.sleep(1)

    # Receber horário:
    Hora = datetime.now()
    Hora_Formatada = Hora.strftime("%H%M")
    Hora_Inteiro = int(Hora_Formatada)

    time.sleep(1)

    if Hora_Inteiro >= 800 and Hora_Inteiro <= 1800:
        mensagem = ""
        pyperclip.copy(mensagem)
        pyautogui.hotkey('ctrl', 'v')

    elif Hora_Inteiro < 800 or Hora_Inteiro > 1800:
        mensagem = ""
        pyperclip.copy(mensagem)
        pyautogui.hotkey('ctrl', 'v')

    # Clicar em Ligar:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    # Fechar página para desligar a ligação:
    time.sleep(51)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()