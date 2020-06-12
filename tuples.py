#Tuple packing
names = ('titus', 'jane', 'doe')

#Tuple unpacking
(first, second, third) = names

#print(first)
#print(second)
#print(third)

(fruit, name, car, country) = ('orange', 'titus', 'renault', 'Norway')

#print(fruit)
#print(name)
#print(car)
#print(country)

x, *y, z = (20, 'coding', 'is', 'dope', 100)
#print(x)
#print(z)
#print(*y)

def multi(x,y):
    return x*y

a = (10,100)

print(multi(*a))