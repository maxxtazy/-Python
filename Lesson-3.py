#Задание 1
a = int(input('Введите делимое число: '))
b = int(input('Введите делитель: '))

def division(a, b):
    if b != 0:
        return a / b
    else:
        print('Ошибка! Деление на 0 невозможно')
print(f'Результат деления = {division(a, b)}')

#Задание 2
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
city = input("Назовите город проживания: ")
email = input("Введите адрес электронной почты: ")
num = input("Введите номер телефона: ")
def user_info(name, surname, year, city, email, num):
    print(f"Имя пользователя: {name}; фамилия: {surname}; год рождения: {year}; город: {city}; email: {email}; номер телефона: {num}")
user_info(name, surname, year, city, email, num)

#Задание 3
def my_func(a, b, c):
    abc_list = [a, b, c]
    abc_list.sort(reverse = True)
    return abc_list[0] + abc_list[1]
print(my_func(1, 2, 3))

#Задание 4.1
def my_func(x, y):
    exp = x**y
    return exp
print(my_func(2, -2))

# Задание 4.2
def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(2, -2))

#Задание 5
def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите несколько чисел или "Q" для выхода - ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Сумма чисел равна {sum_res}')
    print(f'Сумма чисел равна {sum_res}')
my_sum()

#Задание 6
def int_func(a):
     return a.title()
print(int_func('hello'))

#Задание 7
def int_func(*args):
    word = input('Введите слова из строчных латинских букв: ')
    print(word.title())
    return
int_func()