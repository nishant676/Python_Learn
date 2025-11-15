year = 2024
exact_year = int(year)

if(exact_year % 400 ==0) or     (exact_year %4 == 0 and exact_year%100 !=0 ):
    print("leap year")
else:
    print("its not")