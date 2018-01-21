import random

def getGrade(score):
    grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    for grade in sorted(grades):
        if score >= grades[grade]:
            return grade

def reportScore(min, max):
    score = random.randint(min, max)
    print "Score: {0}".format(score) + "; Your grade is " + getGrade(score)


print "Scores and Grades"
for grade in range(0,10):
    reportScore(60, 100)
print "End of the program. Bye!"
