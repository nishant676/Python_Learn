password = "hugy"

count = len(password)
print(count)

if(count <6):
    print("weak")
elif (count <10):
    print("medium")
else:
    print("strong")