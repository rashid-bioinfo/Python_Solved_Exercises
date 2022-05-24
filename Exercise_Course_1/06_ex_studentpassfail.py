''''
Check whether a student is pass or fail
'''

bio = int(input("Please enter the marks of bio: "))
chem = int(input("Please enter the marks of chem: "))
phy = int(input("Please enter the marks of phy: "))

tot_score = 300 # each sub has total 100 score
# Calculcate obtained precentage in 3 subjects
obt_score = ((bio+chem+phy)/tot_score)*100
print("The obtained precentage of the student are: ", obt_score, "% out of total marks ", tot_score)

if (obt_score >= 40.0 and bio >=33 and chem >= 33 and phy >= 33):
    print("The student is pass")
else:
    print("Try again")

