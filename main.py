import requests
from colorama import init, Fore
import time

init()

ps_to_check = input("Place of the texte file to check :")
ps_2 = ''.join(ps_to_check.split("'"))

def test_pseudo(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return response.status_code == 200

with open(f"{ps_2}", "r") as file:
    usernames = file.read().splitlines()

total_usernames = len(usernames)

usernames = [username for username in usernames if len(username) >= 3]

filtered_usernames = len(usernames)
time_to_f = (total_usernames*2)/60

print(f"Number total of names : {total_usernames}")
print(f"Filter with less than 3 characters : {total_usernames - filtered_usernames}")
print(f"The pseudo check was finis in {time_to_f} minutes")


available_usernames = []

for index, username in enumerate(usernames, 1):
    result = test_pseudo(username)
    times = time.strftime("%H:%M:%S", time.localtime())
    status = f"[{times}] [No Available]" if result else f"[{times}] [Available]"
    color = Fore.GREEN if result else Fore.RED
    print(f"{index}/{filtered_usernames} - {username}: {color}{status}{Fore.RESET}")
    
    if result:
        available_usernames.append(username)
        with open("dispo.txt", "a") as dispo_file:
            dispo_file.write(username + '\n')

    if index < filtered_usernames:
        time.sleep(2)  

print("Test de pseudonymes terminé.")

if available_usernames:
    print("Pseudonymes disponibles enregistrés dans dispo.txt")
