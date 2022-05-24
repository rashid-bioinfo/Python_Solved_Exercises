'''
Grading criteria
'''
score = int(input("Please enter the marks of students to check his grade: "))

if (score >= 90 and score <= 100):
    print("Excellent")
if (score >= 80 and score <= 90):
    print("A")
if (score >= 70 and score <= 80):
    print("B")
if (score >= 60 and score <= 70):
    print("C")
if (score >= 50 and score <= 60):
    print("D")
if (score < 50):
    print("Try again")