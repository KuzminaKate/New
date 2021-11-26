import random
a=input("Введите a: ")
b=input("Введите b: ")
c=[]
for i in range(b):
    r=random.randint(a,b)
    c.append(r)
print("Получившийся массив: ", c)
d=min(c)
print("Минимальное число в масиве: ", d)
