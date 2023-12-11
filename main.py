import requests
from colorama import Fore, Style, init
import time
from datetime import datetime


init()

ps_to_check = input("Place of the texte file to check :")
ps_2 = ''.join(ps_to_check.split('"'))
ps_3 = ''.join(ps_2.split("'"))

def test_pseudo(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return response.status_code == 200

with open(f"{ps_3}", "r") as file:
    usernames = file.read().splitlines()

total_usernames = len(usernames)

usernames = [username for username in usernames if len(username) >= 3]

filtered_usernames = len(usernames)
time_to_f = (total_usernames*2)/60
time_to_f_rounded = time_to_f.__round__(1)

print(f"Number total of names : {total_usernames}")
print(f"Filter with less than 3 characters : {total_usernames - filtered_usernames}")
print(f"The pseudo check was finis in {time_to_f_rounded} minutes")


available_usernames = []

for index, username in enumerate(usernames, 1):
    result = test_pseudo(username)
    now = datetime.now()
    times = now.strftime(f"{Fore.BLUE}%H{Style.RESET_ALL}{Fore.BLACK}:{Style.RESET_ALL}{Fore.BLUE}%M{Style.RESET_ALL}{Fore.BLACK}:{Style.RESET_ALL}{Fore.BLUE}%S{Style.RESET_ALL}")
    status = f"{Fore.WHITE}[{Fore.RED}No Available{Fore.WHITE}]" if result else f"{Fore.WHITE}[{Fore.GREEN}Available{Fore.WHITE}]"
    print(f"[{times}]{status}{Fore.RESET} {index}/{filtered_usernames} - {username}")
    
    if not result:
        available_usernames.append(username)
        with open("dispo.txt", "a") as dispo_file:
            dispo_file.write(username + '\n')

    if index < filtered_usernames:
        time.sleep(1.5)  

print("Test de pseudonymes terminé.")

if available_usernames:
    print("Pseudonymes disponibles enregistrés dans dispo.txt")
