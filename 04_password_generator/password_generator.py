import string
import random
def generate_password(length,characters):
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password
def check_strength(password):
    length=len(password)
    has_uppr= any(c.isupper() for c in password)
    has_lower= any(c.islower() for c in password)
    has_digit= any(c.isdigit() for c in password)
    has_symb= any(c in string.punctuation for c in password)
    score= has_uppr + has_lower + has_digit + has_symb
    if length<8:
        return "weak"
    elif score==4 and length>=12:
        return "very strong"
    elif score>=3 and length>=8:
        return "strong"
    elif score==2:
        return "medium"
    else:
        return "weak"
#menu
try:
    length=int(input("Enter length of password: "))
    if length <=7:
        print("Password should be atleast 8 characters long")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()
characters=""
uppercase=input("do you want uppercase in your password (y/n) ")
if uppercase=="y":
    characters+=string.ascii_uppercase
elif uppercase=="n":
    pass
else:
    print("Please enter y or n")
    exit()
lowercase=input("do you want lowercase in your password (y/n) ")
if lowercase=="y":
    characters+=string.ascii_lowercase
elif lowercase=="n":
    pass
else:
    print("Please enter y or n")
    exit()
numbers=input("do you want numbers in your password (y/n) ")
if numbers=="y":
    characters+=string.digits
elif numbers=="n":
    pass
else:
    print("Please enter y or n")
    exit()
symbols=input("do you want symbols in your password (y/n) ")
if symbols=="y":
    characters+=string.punctuation
elif symbols=="n":
    pass
else:
    print("Please enter y or n")
    exit()
if characters=="":
    print("Please select at least one character type")
    exit()
try:
    count=int(input("how many passwords you want to generate: "))
    if count <=0:
        print("Please enter a number greater than 0")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()
for i in range(count):
    password=generate_password(length,characters)
    s=check_strength(password)
    print(f"PASSWORD: {password} | STRENGTH: {s}")
