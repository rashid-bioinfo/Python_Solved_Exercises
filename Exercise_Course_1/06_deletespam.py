'''
Delete the spam
'''
comment = input ("please input your comment:")
spam = "make a lot of money, buy now subscribe this, click this"
if (comment in spam):
    print("spam is found ")
    # deleting the spam
    # text = comment
    text = comment.replace(comment,"hello")
    print("Cleaner text now: ", text)
else:
    print("The comment is safe")