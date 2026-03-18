import random


karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("şifrede ne kadar harf olmalı?"))

parola = ""

for i in range(uzunluk):
    secilen = random.choice(karakter)
    parola += secilen

print(parola)
