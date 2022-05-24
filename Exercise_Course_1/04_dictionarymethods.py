'''
Dictionary methods
'''
rashid = {
    "age" : 34,
    "program" : "PhD",
    "Discipline": "Chemistry",
    "Home": "Eden",
    "kids" : 2,
    "degrees" : ["BS", "MS", "PhD"],
    "kidsage" : {"Zohan" : 2.5, "Azan" : "newborn"} 
}

# print(rashid.items()) # prints all key-value pairs
# print(rashid.keys()) # prints all the keys of the dictionary
# print(rashid.values()) # prints all the values of the dictionary
# rashid.update({"Discipline" : "Computational Chemistry"})
# print(rashid["Discipline"])
# print(rashid.get("kids"))
# print(type(rashid.keys()))
# print(type(rashid.values()))
updateDict = {
    "Research aspirations" : "Computer aided drug design",
    "Discipline" : "Computational Chemistry"
}
rashid.update(updateDict)
print(rashid)