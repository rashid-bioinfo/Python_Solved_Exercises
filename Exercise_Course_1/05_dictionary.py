'''
Example of a dictionary
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
# print(rashid) # prints whole dictionary
# print(rashid["age"])
# rashid["age"] = 35
# print(rashid["age"])
# print(rashid["kidsage"])
# print(rashid["kidsage"]["Zohan"])
# print(rashid["degrees"])

rashid["kidsage"]['Azan'] = 1
print(rashid["kidsage"]['Azan'])