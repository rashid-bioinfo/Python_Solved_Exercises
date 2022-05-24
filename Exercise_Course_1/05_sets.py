'''
Sets in python
'''
# myset = {1,2,3,4,5}
# print(myset)
# print(type(myset))

# Create an empty set
s = set()
print(type(s))
s.add(2)
s.add(3)
s.add(1)
print(s)
# s.add([6,7,8,9]) # This will through an error TypeError: unhashable type: 'list'
s.add((6,7,8,9)) # We can add tupple in set
s.add((1,2,3)) # We can add tupple in set
# s.add({"rashid":"impressive"}) # This will also throw an error
print(s)
print(len(s))
s.remove(2)
print(s)