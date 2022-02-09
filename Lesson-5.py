# Задание 1
with open('file.txt', 'w') as f:
    line = input('Введите строку: ')
    while line:
        f.writelines(line)
        line = input('Введите строку: ')
        if not line:
            break

# Задание 2
f = open('file2.txt', 'r')
content = f.read()
print(f'Содержимое файла: \n{content}')

f = open('file2.txt', 'r')
content = f.readlines()
print(f'Количество строк в файле - {len(content)}')

f = open('file2.txt', 'r')
content = f.read()
words = content.split()
print(f'Количество слов - {len(words)}')
f.close()

# Задание 3
with open('file3.txt', 'r') as f:
    salary = []
    less20 = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            less20.append(i[0])
        salary.append(i[1])
print(f'Оклад менее 20000 имеют: {less20}, средний оклад - {sum(map(int, salary)) / len(salary)}')

# Задание 4
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open('file4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        rus_file.append(rus[i[0]] + ' ' + i[1])

with open('file4rus.txt', 'w') as f2:
    f2.writelines(rus_file)

# Задание 5
def summary():
    try:
        with open('file5.txt', 'w+') as f:
            line = input('Введите цифры через пробел: ')
            f.writelines(line)
            numbers = line.split()
            print(sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

# Задание 6
subj = {}
with open('file6.txt', 'r') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - {subj}')

# Задание 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')