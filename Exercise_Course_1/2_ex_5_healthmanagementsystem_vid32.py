# Health Management System
import datetime

def getdate():
    print(datetime.now())

def retreive_info ():
    

def log_info(user):
    nature = int(input("Please enter 1 for logging info of food and 2 for exercise: "))
    if (nature == 1):
        print("You have chosen to log info of food")
        if (user == 1):
            print("Welcome Rashid to your log book")
            text = input("Please write what food you have taken:\n")
            f=open("rashid_food.txt", "a")
            f.write(text)
            f.write("\n")
            f.close()
        elif (user == 2):
            print("Welcome Andi to your log book")
            f=open("andi_food.txt", "a")
            f.write("")
            f.close()
        elif (user ==3):
            print("Welcome Yasir to your log book")
            f=open("yasir_food.txt", "a")
            f.write("")
            f.close()

getdate()
choice = int(input("Please enter 1 for logging and 2 for retrieving info: "))

getdate()
if (choice == 1):
    print("--- You have chosen to log info ---")
    user = int(input("Please enter 1 for Rashid, 2 for Andi an 3 for yasir: "))
    log_info(user)
    

