
#-----------------------------------------1111111111111111111111111111111111111111111111111
while True:
    a = float(input("первое число: "))
    b = float(input("второе число: "))
    oper = input("какая операция (+, -, *, /): ")

    if oper == '+':
        print(a + b)
    elif oper == '-':
        print(a - b)
    elif oper == '*':
        print(a * b)
    elif oper == '/':
        if b != 0:
            print(a / b)
        else:
            print("на ноль делят только....")
    else:
        print("куда ты жмал?")

    cont = input("продолжить? да/нет:")
    if cont != 'да':
        break
#----------------------------------------------------2222222222222222
n = int(input("Введите число n: "))
summa = 0

for i in range(1, n + 1):
    if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
        summa += i

print("Сумма:", summa)

#------------------------------------------------------333333333
num = input("Введите числа через пробел: ").split()
for i in range(len(num)):
    for j in range(len(num) - i - 1):#сравниваем соседей
        if int(num[j]) > int(num[j + 1]):  
            num[j], num[j + 1] = num[j + 1], num[j]

print("после сортировки получился этот ка...:", num)



#---------------------------------------------------44444444444
text = input("писать тут: ").replace(" ", "").lower()
if text == text[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


#----------------------------------------------------5555555555555555
num = list(map(int, input("числа сюда: ").split()))
most_common = max(num, key=num.count)
print("чаще всего встречается:", most_common)

#------------------------------------------------------666
import random

def ygadai():
    num = random.randint(1, 1000)
    while True:
        vivod = int(input('угадай число: '))
        if vivod == num:
            print("угадал можешь спать спокойно")
            break
        elif vivod > num:
            print("перебор")
        else:
            print("мало половин")
ygadai()

