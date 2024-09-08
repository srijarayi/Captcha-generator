import random
def captcha(length):
    capt=str()
    characters="0123456789"+"abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        capt=capt+random.choice(characters)
    return capt
length=4
print(captcha(length))