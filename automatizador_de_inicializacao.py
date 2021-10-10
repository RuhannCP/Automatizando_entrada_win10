from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import pyautogui
import socket
import sys
import time


def internet(Host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((Host, port))
        socket.setdefaulttimeout(15)
        return True
    except Exception:
        return False


# Função para chamada de um programa
def init_program(name_program):
    pyautogui.press('win')
    pyperclip.copy(name_program)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')


if __name__=="__main__":
    name_game = None
    option_music = None
    estilo = None
    
    pyautogui.PAUSE = 2
    
    if internet() is False:
        pyautogui.click(x=1135, y=745)
        pyautogui.click(x=1198, y=185)
        pyautogui.click(x=1242, y=273)
        pyautogui.sleep(5) 
        
    # Obtendo opcoes
    option = str(input("O que vamos Fazer hoje ?\n (1 - Trabalhar) (2 - Estudar) (3 - Jogar)\n"))
    option_music = str(input("Deseja ouvir uma musica ?(1 - Sim)\n"))
    
    # Obtendo nome do Jogo
    if option == '3':
        name_game = input("Digite o nome do jogo! \n")
    
    # Configuração para abertura do chrome 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-maximized")
    options.add_argument("user-data-dir=C:\\Users\\Ruhann.Ruhann\\AppData\\Local\\Google\\Chrome\\User Data")
    
    # Obtendo tipo de musica
    if option_music == '1':
        style = str(input(" Qual estilo de musica vc deseja ouvir?\n"))
        
        # Iniciando Chrome
        w = webdriver.Chrome(options=options)

        # Iniciando Youtube
        w.get('https://www.youtube.com')
        search_bar = w.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        search_bar.send_keys(style)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        video = w.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[1]/div/a/h3/span')
        time.sleep(1)
        video.click()
    elif option != '3':
        
        # Iniciando Chrome
        w = webdriver.Chrome(options=options)
            
    # Modo trabalho 
    if option == '1':
        w.execute_script('''window.open("https://duckduckgo.com/","_blank");''')
        time.sleep(2)
        init_program('vscode')
        init_program('terminal')
        init_program('telegram')
    
    # Modo estudo
    elif option == '2':
        w.execute_script('''window.open("https://duckduckgo.com/","_blank");''')
        w.execute_script('''window.open("https://virtual.ufmg.br/minhasturmas/","_blank");''')
        time.sleep(2)
        init_program('bloco de notas')
        init_program('telegram')
    
    # Modo jogo
    elif option == '3':
        init_program(name_game)

    sys.exit()    
