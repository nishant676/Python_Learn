def even_generator(limit):
    for i in range(2, limit +1 , 2): # last param means jump with every iteration add 2 step further i+2, 
        yield i
    
for num in even_generator (10):
    print(num)