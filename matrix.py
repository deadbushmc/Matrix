import os
import random
import string
from colorama import Fore, Back, Style

length = 120
a = int(input("Color Picker\n1 for Red\n2 for Blue\n3 for Green\n4 for Yellow\n5 for White"))

while True:
    matrix = ''.join(random.choices(string.digits, k = length))
    last = str(matrix)
    if a == 1:
        print(Fore.RED + last)
    elif a == 2:
        print(Fore.BLUE + last)
    elif a == 3:
        print(Fore.GREEN + last)
    elif a == 4:
        print(Fore.YELLOW + last)
    elif a == 5:
        print(Fore.WHITE + last)