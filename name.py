import random
import string
import colorama
import pyfiglet
from colorama import Fore, Style

colorama.init(autoreset=True)

# Banner oluşturma
banner = pyfiglet.figlet_format("VIOS RIO")
print(Fore.MAGENTA + banner)  # Mor renkte yazdırır

print(Fore.YELLOW + "----------------------------")
print(Fore.CYAN + "|      Generator İsim      |")
print(Fore.YELLOW + "----------------------------\n")

# Kullanıcıdan isim al
base_name = input(Fore.GREEN + "İsim Seç: ")

# Kullanıcıdan kaç adet üretmek istediğini al
try:
    count = int(input(Fore.BLUE + "Kaç adet üretmek istiyorsun? "))
except ValueError:
    print(Fore.RED + "Hata: Sayı girmen lazım!")
    exit()

def generate_random_usernames(base_name, count):
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]
    usernames = set()  # Aynı isimleri tekrar üretmemesi için set kullanıyoruz
    
    while len(usernames) < count:
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 6)))
        usernames.add(base_name + random_suffix)

    print("\n" + Fore.YELLOW + "---- Üretilen Kullanıcı Adları ----\n")
    for username in usernames:
        print(random.choice(colors) + username)

generate_random_usernames(base_name, count)
