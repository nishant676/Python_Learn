score = 125
total_score = int(score)

if(total_score >= 101):
    print("please verify ur score again")
    exit() #-----> use as return in java means exit program

if(total_score >= 90):
    grade = "A"
elif(total_score >=80):
    grade = "B"
elif(total_score >=70):
    grade = "C"
elif(total_score >=60):
    grade = "D"
else:
    grade = "F"

print(grade)