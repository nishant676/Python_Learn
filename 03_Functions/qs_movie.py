age = input("Whats ur age?")
age_score = int(age)
day = "wednesday"

# if(age_score<18):
#     if(day == "wednesday"):
#         print("8$ but we also get 2$ discount")
#     else:
#         print("$8 for the movie")
# else:
#     if(day == "wednesday"):
#         print("12$ but we also get 2$ discount")
#     else:
#         print("$12 for the movie")

#-----------------------------------OR-----------------------

price = 12 if age_score >=18 else 8

if(day == "wednesday"):
    price -= 2
print("Ticket price for u is $" ,price)