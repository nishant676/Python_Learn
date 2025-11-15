chai_types = {"Masala":"Spicy", "Ginger":"Zesty", "Green":"Mild"}

print(chai_types["Ginger"]) #o/p:-Zesty

# change value

chai_types["Green"] = "Fresh"
print(chai_types) #o/p:{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# get():-
print(chai_types.get("Green")) #o/p:-Mild

# Loop

for chai in chai_types:
    print(chai) #o/p:Fresh ,Masala, Ginger,Green ===> all keys are printed

for chai in chai_types:
    print(chai,"-" ,chai_types[chai]) #o/p:Masala - Spicy,Ginger - Zesty, Green - Fresh


# Another Method
for key, value in chai_types.items():
    print(key,value) #o/p:Masala Spicy,Ginger Zesty,Green Fresh

if "Masala" in chai_types:
    print("I have it")

#Length
print(len(chai_types)) #o/p:-3 ===> 3 pair present 


# pop():-
# => need to write key to delete
chai_types.pop("Ginger")
print(chai_types)#o/p:-{'Masala': 'Spicy', 'Green': 'Fresh'}

#popitems():-
#=> delete value from last
print(chai_types.popitem()) #o/p:('Green', 'Fresh')


chai_types["Mix"] = "Sweet"
chai_types["Cofee"] ="latte"

# del:-
#===> used to delete 
del chai_types["Mix" ]
print(chai_types)#o/p:{'Masala': 'Spicy', 'Cofee': 'latte'}


# squard number
square_num = {x:x**2 for x in range(5)} 
print(square_num) #o/p:{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

square_num.clear() #====> clear all

keys = ["masala", "ginger", "lemon", "herbal"]
default_value = "delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict) #o/p:-{'masala': 'delicious', 'ginger': 'delicious', 'lemon': 'delicious', 'herbal': 'delicious'}