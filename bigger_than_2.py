try:
    num = int(input("Type a number: "))
    if num > 2:
        print("Oh yeah, that number is bigger than 2.")
    elif num == 2:
        print("Hey, who are you trying to fool?")
    else:
        print("No, 2 is bigger than that puny number.")
except:
    print("ERROR DETECTED")
