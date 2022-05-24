'''
Create a dictionary of English words
'''

mydict = {
    "arduous" : "painful",
    "staunch" : "keen",
    "absconder" : "proved guilty and has fled"
}
# Basic operation on dictionaries
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
print("You can look up the meanings of following words: ", mydict.keys())
# print(mydict["arduous"])
ch = input ("Please enter a word you want to see the meanings: ")
# print(mydict[ch])
print(mydict.get(ch))