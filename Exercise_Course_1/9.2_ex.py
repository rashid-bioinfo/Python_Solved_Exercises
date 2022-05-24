import random

def game():
    randNo = random.randint(1,100000)
    return randNo
    

with open("hiscore.txt", 'r') as f:
    a = f.read()

b = game()
print(b)
if b > int(a):
    with open("hiscore", 'w') as f:
        f.write(str(b))