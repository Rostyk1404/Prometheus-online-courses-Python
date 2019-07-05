import sys

"""Практичне завдання №4.1
0.0/1.5 балів (оцінено)
Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити пробіли, літери латинського
алфавіту в будь-якому регістрі та цифри. Для передачі одним значенням рядок, що містить пробіли, береться в подвійні лапки.

Результат роботи: рядок "YES", якщо отриманий рядок є паліндромом, або "NO" - якщо ні. Рядок вважається паліндромом,
якщо він однаково читається як зліва направо, так і справа наліво. Відмінністю регістрів та пробілами знехтувати.

Наприклад
Вхідні дані: 0
Приклад виклику: python lab4_1.py 0
Результат: YES
Вхідні дані: puppy
Приклад виклику: python lab4_1.py puppy
Результат: NO
Вхідні дані: "mystring1Gni rts ym"
Приклад виклику: python lab4_1.py "mystring1Gni rts ym"
Результат: YES"""
# Sample 1

#
# a = str(sys.argv[1])
# a = a.lower().replace(" ", "")
#
# if a == a[::-1]:
#     print("YES")
# else:
#     print("No")

# Sample 2


"""Практичне завдання №4.2
1.5/1.5 балів (оцінено)
Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. 
Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.

Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. 
Пробіл в кінці рядка відсутній.

Наприклад
Вхідні дані: 1
Приклад виклику: python lab4_3.py 1
Результат: 1
Вхідні дані: qwe asd zxc 123
Приклад виклику: python lab4_3.py qwe asd zxc 123
Результат: 123 zxc asd qwe
Вхідні дані: padawan young my HAVE MUST YOU PATIENCE
Приклад виклику: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
Результат: PATIENCE YOU MUST HAVE my young padawan
"""
# Sample 1

a = sys.argv[1:]
a.reverse()
res = a[0]
for x in a[1:]:
    res = res + " " + x

# Sample 2

a = sys.argv[1:]
c = " ".join(a[::-1])
# print(c)


"""Практичне завдання №4.3
2.0/2.0 бали (оцінено)
Вхідні дані: рядок, що складається з відкриваючих та закриваючих круглих дужок - аргумент командного рядка. 
Для передачі в якості рядка послідовність береться в подвійні лапки.

Результат роботи: рядок "YES", якщо вхідний рядок містить правильну дужкову послідовність; або рядок "NO", 
якщо послідовність є неправильною. Дужкова послідовність вважається правильною, якщо всі дужки можна розбити попарно 
"відкриваюча"-"закриваюча", при чому в кожній парі закриваюча дужка слідує після відкриваючої.

Пояснення для математиків:
"" (порожній рядок) - правильна дужкова послідовність (ПДП)
"(ПДП)" - також ПДП
"ПДППДП" (дві ПДП записані поряд) - також ПДП

Наприклад
Вхідні дані: ")("
Приклад виклику: python lab4_3.py ")("
Результат: NO
Вхідні дані: "(()(()"
Приклад виклику: python lab4_3.py "(()(()"
Результат: NO
Вхідні дані: "(()(()()))"
Приклад виклику: python lab4_3.py "(()(()()))"
Результат: YES
Вхідні дані: "())()(()())(()"
Приклад виклику: python lab4_3.py "())()(()())(()"
Результат: NO"""
# Sample 1

data = sys.argv[1]
counter = 0

for x in data:
    if x == "(":
        counter += 1
    elif x == ")":
        counter -= 1
    if counter < 0:
        flag = False
if True and counter == 0:
    print("YES")
else:
    print("NO")


# Sample 2
def brackets(data):
    counter = 0
    for x in data:
        if x == "(":
            counter += 1
        elif x == ")":
            counter -= 1
        if counter < 0:
            return "NO"
    if counter == 0:
        return "YES"
    else:
        return "NO"


# print(brackets(")("))
# print(brackets("(()(()()))"))
# print(brackets("(()(()"))
# print(brackets("())()(()())(()"))

"""Практичне завдання №4.4
2.0/2.0 бали (оцінено)
Завдання передбачає пошук "щасливих" квитків. "Щасливим" називається такий тролейбусний квиток, в якому сума перших 
трьох цифр дорівнює сумі останніх трьох. Наприклад 030111 (0+3+0 = 1+1+1), 902326 (9+0+2 = 3+2+6), 001100 (0+0+1 = 1+0+0).

Вхідні дані: два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного рядка.

Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до a2 включно. 
Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, 
як це і відбувається при нумерації квитків. Виводити номери квитків не треба.

Наприклад
Вхідні дані: 0 1000
Приклад виклику: python lab4_4.py 0 1000
Результат: 1
Пояснення: номер 000000
Вхідні дані: 1001 1122
Приклад виклику: python lab4_4.py 1001 1122
Результат: 3
Пояснення: номери 001001, 001010, 001100
Вхідні дані: 222222 222333
Приклад виклику: python lab4_4.py 222222 222333
Результат: 7
Пояснення: номери 222222, 222231, 222240, 222303, 222312, 222321, 222330"""


# Sample 1
def lucky_tickets(n, m):
    counter = 0
    for x in range(n, m + 1):
        tickets = list(str(x))
        ticket0 = [0 for i in range(6 - (len(tickets)))]
        lucky_ticket = ticket0 + tickets
        if (int(lucky_ticket[0]) + int(lucky_ticket[1]) + int(lucky_ticket[2]) == int(lucky_ticket[3]) +
                int(lucky_ticket[4]) + int(lucky_ticket[5])):
            counter += 1
    return counter


# Sample 2

a = int(sys.argv[1])
b = int(sys.argv[2])
counter = 0
for x in range(a, b + 1):
    x_to_str = list(str(x))
    ticket0 = [0 for i in range(6 - (len(x_to_str)))]
    result = ticket0 + x_to_str
    if int(result[0]) + int(result[1]) + int(result[2]) == int(result[3]) + int(result[4]) + int(result[5]):
        counter += 1