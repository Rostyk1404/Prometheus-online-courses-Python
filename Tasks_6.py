"""Практичне завдання 6.1
1.5/1.5 балів (оцінено)
Розробити функцію count_holes(n),
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами (вважати, що у "4"
та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом.

пояснення щодо отворів в цифрах

Незначущими нулями на початку запису числа, якщо такі є, нехтувати.

Наприклад
Виклик функціїі: count_holes('123')
Повертає: 0
Виклик функціїі: count_holes(906)
Повертає: 3
Виклик функціїі: count_holes('001')
Повертає: 0
Виклик функціїі: count_holes(-8)
Повертає: 2
Виклик функціїі: count_holes(-8.0)
Повертає: ERROR"""


def count_holes(holes):
    try:
        if isinstance(holes,float):
            raise
        holes = abs(int(holes))

        dict_of_holes = {"9": 1, "8": 2, "7": 0, "6": 1, "5": 0, "4": 1, "3": 0, "2": 0, "1": 0, "0": 1}
        count = 0
        for x in str(holes):
            count += dict_of_holes[x]
    except:
        return 'ERROR'
    return count

print(count_holes(-8.0))


"""Практичне завдання 6.2
2.0 можливих бали (оцінено)
Розробити функцію encode_morze(text), 
яка приймає 1 аргумент -- рядок, 
та повертає рядок, який містить діаграму сигналу, що відповідає переданому тексту, закодованому міжнародним кодом Морзе 
для англійського алфавіту. Розділові та інші знаки, що не входять до латинського алфавіту, ігнорувати. 
Регістром літер нехтувати.

Morze code

Для передачі повідомлення за одиницю часу приймається тривалість однієї крапки. Тривалість тире дорівнює трьом крапкам. 
Пауза між елементами одного знака -- одна крапка, між знаками в слові -- 3 крапки, між словами -- 7 крапок. 
Словом вважати послідовність символів, обмежена пробілами. Результуюча "діаграма" демонструє наявність сигналу в кожний 
проміжок часу: на і-й позиції знаходиться "^", якщо в цей момент передається сигнал, і "_", якщо сигналу немає. 
Зайві паузи в кінці повідомлення на "діаграмі" відсутні.

Пояснення

Наприклад
Виклик функції: encode_morze('Morze code')
Повертає: ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^
Виклик функції: encode_morze('Prometheus')
Повертає: ^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
Виклик функції: encode_morze('SOS')
Повертає: ^_^_^___^^^_^^^_^^^___^_^_^
Виклик функції: encode_morze('1')
Повертає:"""

"""Практичне завдання 6.3
2.0 можливих бали (оцінено)
Розробити функцію saddle_point(matrix), 
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків, 
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та 
максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки 
мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його 
списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).

Наприклад
1 2 3
3 2 1
Виклик функції: saddle_point([[1,2,3],[3,2,1]])
Повертає: False
8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
Виклик функції: saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
Повертає: (1, 2)
21
Виклик функції: saddle_point([[21]])
Повертає: (0, 0)"""

"""Практичне завдання 6.4
1.5 можливих балів (оцінено)
Розробити функцію find_most_frequent(text), 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']"""