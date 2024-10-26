from random import randint

print("This program will generate burner email addresses for you\nNOTE: the odds that these addresses are in English or any other discernable language are slim to none.")

def builder(choice, funny):

    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    num_num = 0
    num_let = 0
        
    if choice == 1:
        rand = randint(0, len(numbers)-1)
        funny+=numbers[rand]
    elif choice == 2:
        rand = randint(0, len(letters)-1)
        funny+=letters[rand]
    return funny

domains = ["gmail.com", "hotmail.com", "outlook.com"]

email = ""

while len(email) <= 10:
    switch = randint(1, 2)

    if (switch == 1):
        email = builder(1, email)
    elif (switch == 2):
        email = builder(2, email)

dom = randint(0,2)

newmail = email+"@"+domains[dom]
print("\n"+newmail)
