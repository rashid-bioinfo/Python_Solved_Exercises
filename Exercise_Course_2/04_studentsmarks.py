'''
Accept marks of 6 students and display them in a sorted manner
'''

shahid = int(input ("Please enter marks of shahid: "))
rashid = int(input ("Please enter marks of rashid: "))
asghar = int(input ("Please enter marks of asghar: "))
nadeem = int(input ("Please enter marks of nadeem: "))
azam = int(input ("Please enter marks of azam: "))
bilal = int(input ("Please enter marks of bilal: "))

marks = [shahid, rashid, asghar, nadeem, azam, bilal]
print ("marks without sorting: ", marks)
marks.sort()
print ("marks with sorting: ", marks)