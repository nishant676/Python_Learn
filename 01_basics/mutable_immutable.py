h1 = [1,2,3]
h2 = h1[:] # [:]---> means all data , if [0:2]--> here 0 inclusive & 2exclusive
h1[0] = 34
print(h1) #o/p--> [34, 2, 3]
print(h2) # o/p--->[1, 2, 3] ===> cause here by using [:] we copied value from h1 not triggering its refernece so, any change will not give impact

#------------------------------------------------------------------

myteam = [1,2,3,4]
myteam2 = myteam
myteam[0]= 22
print(myteam) #o/p-->[22, 2, 3, 4]
print(myteam2) #o/p--->[22, 2, 3, 4]==> here we trigger myteam refeence so, change will impact 

#------------------------------------------------------------------

hero = [1,2,3,4]
hero2 = hero
hero[0] = 55
hero2 = [1,2,3,4]
print(hero) # o/p---> [55, 2, 3, 4]
print(hero2)# o/p--->[1, 2, 3, 4]

#------------------------------------------------------------------

m = [1,2,3]
n = m
print(m == n) # o/p--> True ==> cause its checking value
print(m is n) # o/p--->True ==> cause both indicate same refference

n = [1,2,3]
print(m == n)  # o/p--> True ==> cause its checking value & value is same for both
print(m is n)  # o/p--> False ==> cause reference/obj is diff for both 

