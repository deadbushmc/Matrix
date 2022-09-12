import os
import random
import string
from colorama import Fore, Back, Style

length = 120

while True:
    matrix = ''.join(random.choices(string.digits, k = length))
    last = str(matrix)
    print(Fore.GREEN + last)