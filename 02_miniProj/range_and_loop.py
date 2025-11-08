numbers = range(7) # 0 1 2 3 4 5 6---> here 0 to n-1

print(numbers) #----> o/p = range(0,7)

#Loops

#1. While loop

i = 1
while i <= 5:
    print(i)
    i+=1

# 2. For loop

for item in range(6):
    print(item+10)


# List

marks = [95, 100 ,45]
print(marks) #---> all value print
print(marks[0:2]) #---> o/p == 95, 100 ==> in param start and till second parm index
print(marks[1]) # here it will print index base value "100"
print(marks[-1]) #---->ans: 45 ===> start checking from last ward 
print(marks[-2]) #---->ans: 100 ===> start checking from last


day = ["wed", "Thu", "Fri"]

for weekday in day:
    print(weekday)

## List ---> Append===> add at the last 

day.append("sat")
print(day)

## List ---> insert(index, new value)====> add value in the particular index

day.insert(0,"Tue" )

print(day)

## List---> in ()==> used to check that present in the list or not

print("Tue" in day) # true

print('***********')
## List---> len(list name) ===> return lenght of the list

print(len(day)) #---> o/p== 5
i = 0 
while i < len(day):
    print(day[i])
    i+=1

# List---> clear()=====> make that list empty

day.clear()
print(day) #----> o/p===> []
