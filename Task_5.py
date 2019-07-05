"""Завдання 5.1
 Додати цю сторінку до закладок
Практичне завдання 5.1
0/1.5 балів (оцінено)
Розробити функцію clean_list(list_to_clean),
яка приймає 1 аргумент -- список будь-яких значень (рядків, цілих та дійсних чисел) довільної довжини,
та повертає список, який складається з тих самих значень, але не містить повторів елементів.
Це значить, що у випадку наявності значення в початковому списку в кількох екземплярах перший "екземпляр" значення
залишається на своєму місці, а другий, третій та ін. видаляються.

Наприклад
Виклик функції: clean_list([1, 1.0, '1', -1, 1])
Повертає: [1, 1.0, '1', -1]
Виклик функції: clean_list(['qwe', 'reg', 'qwe', 'REG'])
Повертає: ['qwe', 'reg', 'REG']
Виклик функції: clean_list([32, 32.1, 32.0, -123])
Повертає: [32, 32.1, 32.0, -123]
Виклик функції: clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
Повертає: [1, 2, 3, 4, 5, 6, '2', 7, 8, 9, 0]"""


def clean_list(list_to_clean):
    new_list = []
    for x in list_to_clean:
        type_x = type(x)
        if x not in new_list:
            new_list.append(x)
        if x in new_list:
            if type(x) is not type(new_list[new_list.index(x)]):
                new_list.append(type_x(x))
    return new_list


# print(clean_list([1, 1.0, '1', -1, 1]))
# print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
# print(clean_list([32, 32.1, 32.0, -123]))
# print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))

# def test_clean_list():
#     input_values = clean_list([1, 1.0, '1', -1, 1])
#     expexted_result = [1, 1.0, '1', -1]
#     assert input_values == expexted_result
# test_clean_list()

"""Практичне завдання 5.2
0.0/1.5 балів (оцінено)
Розробити функцію counter(a, b),
яка приймає 2 аргументи -- цілі невід'ємні числа a та b,
та повертає число -- кількість різних цифр числа b, які містяться у числі а.

Наприклад
Виклик функції: counter(12345, 567)
Повертає: 1
Виклик функції: counter(1233211, 12128)
Повертає: 2
Виклик функції: counter(123, 45)
Повертає: 0"""


def counter(a, b):
    a_str = set(a)
    b_str = set(b)
    return len(a_str & b_str)


"""Практичне завдання 5.3
2.0 можливих бали (оцінено)
Розробити функцію super_fibonacci(n, m),
яка приймає 2 аргументи -- додатні цілі числа n та m (0 < n, m <= 35),
та повертає число -- n-й елемент послідовності супер-Фібоначчі порядку m.

Нагадуємо, що послідовність Фібоначчі -- це послідовність чисел, в якій кожний елемент дорівнює сумі двох попередніх.
Послідовністю супер-Фібоначчі порядку m будемо вважати таку послідовність чисел, в якій кожний елемент дорівнює
сумі m попередніх. Перші m елементів (з порядковими номерами від 1 до m) вважатимемо одиницями.

Наприклад
Виклик функції: super_fibonacci(2, 1)
Повертає: 1
Виклик функції: super_fibonacci(3, 5)
Повертає: 1
Виклик функції: super_fibonacci(8, 2)
Повертає: 21
Виклик функції: super_fibonacci(9, 3)
Повертає: 57"""

# def super_fibo(a,b):


"""Практичне завдання 5.4
0.0/2.0 бали (оцінено)
Розробити функцію file_search(folder, filename), 
яка приймає 2 аргументи -- список folder та рядок filename, 
та повертає рядок -- повний шлях до файлу або папки filename в структурі folder.

Файлова структура folder задається наступним чином:

Список -- це папка з файлами, його 0-й елемент містить назву папки, а всі інші можуть представляти або файли в цій папці
(1 файл = 1 рядок-елемент списку), або вкладені папки, які так само представляються списками. 
Як і в файловій системі вашого комп'ютера, шлях до файлу складається з імен всіх папок, в яких він міститься, 
в порядку вкладеності (починаючи з зовнішньої і до папки, в якій безпосередньо знаходиться файл), розділених "/".

Вважати, що імена всіх файлів є унікальними. Повернути логічне значення False, якщо файл не знайдено.

Наприклад
Виклик функції: file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
Повертає: 'C:/ideas.txt'
Виклик функції: file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 
'find.me.bak' ] ], 'hey.py'], 'find.me')
Повертає: False
Виклик функції: file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', 
['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
Повертає: '/home/user2/desktop/new folder/hereiam.py'

Лапки не повертаються і використані тут для розрізнення логічного False та рядків."""

def file_search(folder, filename):
    result = []
    for item in folder:
        if isinstance(item, list):
            item[0] = f'{folder[0]}/{item[:]}'
            res = file_search(item, filename)
            if res:
                result.extend(res)
        elif item == filename:
            result.append(f"{folder[0]},{item[0:]}")
    return result


def file_search2(folder, filename):
    if folder == filename:
        return filename
    else:
        if folder == filename:
            return filename
        else:
            if isinstance(folder, list):
                if folder[0] == filename:
                    return filename
                for item in folder[1:]:
                    path = file_search2(item, filename)
                    if isinstance(path, str):
                        return folder[0] + '/' + path
                return False
    return False
