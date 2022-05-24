
f = open("Sample.txt", 'r')
a = f.read()
f.close()

if "donkey" in a:
    b = a.replace("donkey","#####")
# print(b)
f = open("Sample.txt", 'w')
f.write(b)
f.close()


# with open("Sample.txt", 'w') as f:
#     a = f.write(b)
    
