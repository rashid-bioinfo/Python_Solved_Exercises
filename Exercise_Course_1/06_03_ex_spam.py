
text = input ("Please input your text\n ")

if ("buy now" in text):
    spam = True
elif ("make a lot of money" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This text is spam")
else:
    print("This text is NOT spam")



