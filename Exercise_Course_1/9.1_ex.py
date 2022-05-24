with open('poems.txt', 'r') as f:
    a = f.read()
if "twinkle" in a:
    print("twinkle word is present in string")
else:
    print("twinkle word is NOT present in string")
