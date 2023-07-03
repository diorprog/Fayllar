                #
                
def square(n):
    for i in range(n):
        yield i*i

q=square(5)                 #q --> generator
for i in q:
    print(i)