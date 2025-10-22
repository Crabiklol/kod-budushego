name = input("Text your name - ")
age = int(input("Text your age- "))
print 



zad1 = int(input("введите 1 число - "))
zad2 = int(input("введите 2 число - "))
zad3 = int(input("введите 3 число - "))
a = (zad1+zad2+zad3)
print (a)



a = int(input("НАПИШИТЕ ЧИСЛО - "))
if (a %2 == 0):
    print("четно")
else :
    print("нечетно")
 
 
    
a = int(input("введите 1 число - "))
b = int(input("введите 2 число - "))
if (a>b):
    print(a)
elif (b>a):
    print(b)
else:
    print("числа равны")



a = int(input("сколько вам лет - "))
if (a>=18):
    print(f"Вам {a}, вы получаете права")
else:
    print(f"Вам {a}, потерпите до 18 перед тем как хасанить")
 
 
    
a = int(input("введите любое число - "))
if a > 0:
    a = a + 1
elif a < 0:
    a = a - 2
elif a == 0:
    a = 0
print(a)



a = int(input("введите год - "))
if (a%4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("год високосный")
else:
    print("год не високосный")



