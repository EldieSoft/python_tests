import random

length = random.randint(8,20)
pword = 0
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26
lower = "abcdefghijklmnopqrstuvwxyz" #26
number = "12345678901234567890123456" #26
special = "!@#$%^&*()?/_=-+.`~{}[];:," #26
new_pword = ""

def getChar(string, num):
    return string[num]

def getList(num, rand):
    match num:
        case 1:
           x = getChar(caps, rand)
           return x
        case 2:
           x = getChar(lower, rand)
           return x
        case 3:
           x = getChar(number, rand)
           return x
        case 4:
           x = getChar(special, rand)
           return x

while (pword <= length):
    rand_char = random.randint(0,25)
    rand_list = random.randint(1,4)
    
    newPword = getList(rand_list, rand_char)
    new_pword+=newPword
    pword+=1
print("The new password is:", new_pword)
