import time
import pyautogui
import pyperclip
from datetime import datetime

# Contar quantas vezes o código rodou:
Contador_1 = 0

while True:
    # Atualizar chamados:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    # Atualizar menu:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    # Clicar no chamado:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    # Tratamento de possível bug (Recarregar site):
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

    '''Logica para reconhecer se existe chamado aberto:'''

    # Coordenadas iniciais e finais do texto a ser copiado:
    time.sleep(1)
    x_inicial, y_inicial = ()
    x_final, y_final = ()

    # Mover o mouse até a posição inicial, segurando botão esquerdo:
    time.sleep(2)
    pyautogui.moveTo(x_inicial, y_inicial)
    time.sleep(1)
    pyautogui.mouseDown()

    # Mover o mouse até a posição final, solta o botão esquerdo:
    time.sleep(2)
    pyautogui.moveTo(x_final, y_final)
    time.sleep(1)
    pyautogui.mouseUp()

    # Clicar com botão direito no meio do texto:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.rightClick()

    # Copiar o texto para obter a informação de chamado:
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    # Obter o texto copiado da área de transferência:
    time.sleep(1)
    texto_copiado = pyperclip.paste()

    # Tratamento de possível bug (explorador de arquivos abre):
    time.sleep(2)
    pyautogui.moveTo()
    time.sleep(1)
    pyautogui.click()

    '''Logica para verificar o texto copiado:'''

    # Variáveis de chamada e horário:
    chamada_realizada = False
    Hora_Formatada = ""

    # As condição abaixo, filtram o resultado e executam a ação de acordo:
    if texto_copiado == "Aberto)" and not chamada_realizada:

        # Informar hora do chamado:
        Hora = datetime.now()
        Hora_Formatada = Hora.strftime("%H:%M")
        print("Chamado reconhecido às:", Hora_Formatada)

        # Clicar em ações:
        time.sleep(2)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em reconhecer chamado:
        time.sleep(2)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em salvar:
        time.sleep(3)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Atualizar menu:
        time.sleep(2)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Atualizar a variável para indicar que a função foi executada e ligar:
        chamada_realizada = True

        from funcoes import realizar_chamada

        realizar_chamada()

    elif texto_copiado == " Aberto)" and not chamada_realizada:

        # Informar hora do chamado:
        Hora = datetime.now()
        Hora_Formatada = Hora.strftime("%H:%M")
        print("Chamado reconhecido às:", Hora_Formatada)

        # Clicar em ações:
        time.sleep(2)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em reconhecer chamado:
        time.sleep(3)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em salvar:
        time.sleep(3)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Atualizar menu:
        time.sleep(2)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Atualizar a variável para indicar que a função foi executada e ligar:
        chamada_realizada = True

        from funcoes import realizar_chamada

        realizar_chamada()

    else:
        # Informar hora:
        Hora = datetime.now()
        Hora_Formatada = Hora.strftime("%H:%M")
        print("Nenhum chamado às:", Hora_Formatada)

    '''Logica para reiniciar página a cada 30 vezes que o código rodar:'''

    # Atualiza a variável:
    Contador_1 += 1

    # A condição abaixo, recarrega a página de acordo com o solicitado:
    if Contador_1 == 30:
        # Clicar em "atualizar" no navegador:
        time.sleep(1)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em "recarregar" no PopUp:
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()

        # Clicar em "Login":
        time.sleep(5)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em "Pesquisar":
        time.sleep(5)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Clicar em "Monitor de enventos":
        time.sleep(1)
        pyautogui.moveTo()
        time.sleep(1)
        pyautogui.click()

        # Atualizar a variável:
        Contador_1 = 0