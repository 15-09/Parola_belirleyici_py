import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Şifreniz kaç harfli olsun?"))
password = ""

for i in range(length):
    
    password += random.choice(characters)
print(password)        