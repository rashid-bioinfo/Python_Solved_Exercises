'''
Snake, water, gun game
'''
import random

def gameWin(you,comp):
    if you == comp:
        return None
    if you == 'g':
        if comp == 'w':
            return False
        elif comp == 's':
            return True    
    elif you == 's':
        if comp == 'w':
            return True
        elif comp == 'g':
            return False    
    elif you == 'w':
        if comp == 'g':
            return True
        elif comp == 's':
            return False    

you = input("Please choose snake(s), water(w), gun(g): ")

randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

print(f"You chose : {you}")
print(f"Comp chose: {comp}")

a = gameWin(you,comp)

if a == None:
    print("Tie the game")
elif a == True:
    print("You won!")
else:
    print("You lose!")






