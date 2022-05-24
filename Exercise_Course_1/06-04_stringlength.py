'''
Character length
'''

username = input("Please input your name: ")

if (len(username) < 10):
    print("The user",username, " contains less than 10 characters (",len(username), ")")
else:
    print("The user",username, " contains more than 10 characters (",len(username), ")")

