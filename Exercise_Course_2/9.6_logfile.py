
with open("log.txt", 'r') as f:
    a = f.read()

if 'python' in a.lower():
    print("python is found in text")
else:
    print("python is NOT found in text")