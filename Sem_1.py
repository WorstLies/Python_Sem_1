# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n=int(input("введите 1-ое число: "))
m=int(input("Введите 2-ое число: "))
k=int(input("Введите 3-ое число: "))
sum=n+m+k
print(sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int(input())
b = int((a/3)*2)
c = int((b/2)/2)
s = int(c)
print(c, b, s)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

a = [int(i) for i in input("Введите шестизначное число билета: ")]
if sum(a[:3]) == sum(a[3:]):
    print('YES')
else:
    print('NO')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n,m,k = int(input("Введите длину шоколадки: ")),int(input("Введите ширину шоколадки: ")),int(input("Введите количество долек: "))
if n*m>k:
    if k%n == 0 or k%m==0:
        print('YES')
    else:
        print ('NO')
else:
    print ('NO')