import pyautogui
import time

# Função para realizar o processo de renovação do certificado
def renovar_certificado(codigo):
    # Clicar em "Editar"
    pyautogui.click(719, 884)
    time.sleep(1)

    # Clicar em "Código"
    pyautogui.click(678, 316)
    time.sleep(1)

    # Ler o código do arquivo de texto
    pyautogui.write(codigo)
    pyautogui.press('enter')
    time.sleep(1)

    # Clicar em "Certificados Digitais"
    pyautogui.click(1054, 283)
    time.sleep(1)

    # Clicar em "Tipo de Certificado" 
    pyautogui.click(776, 342)
    time.sleep(1)

    # Clicar em "Modelo de Certificado" 
    pyautogui.click(730, 385)
    time.sleep(1)

     # Clicar em "Tipo de certificado" novamente 
    pyautogui.click(776, 342)
    time.sleep(1)

    # Clicar em "Adicionar Certificado" 
    pyautogui.click(722, 363)
    time.sleep(1)

    # Clicar em "Gravar"
    pyautogui.click(812, 884)
    time.sleep(1)

    # Clicar em "Empresas" para voltar ao início do processo
    pyautogui.click(500, 283)
    time.sleep(1)

# Abrir o arquivo de texto com os códigos
with open('codigos2401.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Iterar através das linhas e renovar os certificados
for linha in linhas:
    codigo = linha.strip()  # Remover espaços em branco e quebras de linha
    renovar_certificado(codigo)
