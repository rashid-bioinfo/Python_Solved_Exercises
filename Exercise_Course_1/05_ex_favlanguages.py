'''
Allow 4 friends to enter their favourit languages
'''

mydict = {}
A = input("Zulqurnain, Please enter your favourite language: ")
B = input("Mohsin, Please enter your favourite language: ")
C = input("Rashid, Please enter your favourite language: ")
D = input("Jawad, Please enter your favourite language: ")
mydict = {
    "Zulq" : A,
    "Mohsin" : B,
    "Rashid" : C,
    "Jawad" : D
}
print(mydict.items())