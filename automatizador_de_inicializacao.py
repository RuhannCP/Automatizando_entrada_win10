# To add a new cell, type ''
import pyperclip
import pyautogui
import sys


if __name__=="__main__":
    name_game = None
    option = input("O que vamos Fazer hoje ?\n (1 - Trabalhar) (2 - Estudar) (3 - Jogar)\n")
    estilo = input("Qual o estilo de musica vamos ouvir hoje ?\n")

    # Obter nome do jogo
    if option == '3':
        name_game = input('Digite o nome do jogo\n')


    # Inicializando playlist
    pyautogui.press('win')
    pyautogui.sleep(2)
    pyperclip.copy(r'chrome')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.sleep(7)
    pyautogui.hotkey('win','up')
    pyautogui.hotkey('win','up')
    pyautogui.hotkey('ctrl','l')
    pyperclip.copy(r'youtube.com')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

    # Trabalhar
    if option == '1':

        # Buscando playlist
        pyautogui.sleep(5)
        pyautogui.click(x=1929, y=59)
        pyautogui.sleep(2)
        pyperclip.copy(r'playlist para ouvir no Trabalho '+estilo)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.click(x=1885, y=636)
        
        # Iniciando área de trabalho
        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy(r'chrome')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(2)

        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy(r'vscode')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(2)
        
        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy(r'telegram')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(2)

        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy(r'terminal')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(2)

    # Estudar    
    elif option == '2':

        # Buscando playlist
        pyautogui.sleep(5)
        pyautogui.click(x=1929, y=59)
        pyautogui.sleep(2)
        pyperclip.copy('playlist para ouvir estudando '+estilo)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.click(x=1885, y=636)
        
        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy('chrome')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.click(x=2274, y=440)
        
        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy('bloco de notas')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        

    # Jogar
    elif option == '3':
        
        # Buscando playlist    
        pyautogui.sleep(5)
        pyautogui.click(x=1929, y=59)
        pyautogui.sleep(2)
        pyperclip.copy(r'playlist para ouvir jogando '+estilo)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.click(x=1885, y=636)
        
        pyautogui.press('win')
        pyautogui.sleep(2)
        pyperclip.copy(name_game)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')

    # Comando usado para saber posicao do mouse 
    # pyautogui.sleep(5)
    # pyautogui.position()


sys.exit()    



