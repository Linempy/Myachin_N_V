# # -*- coding: utf-8 -*-

print('Курс Основы программирования начался')  ,#задание №1
print('--------------')

print(16823 * 12302 % 3092) #задание №2
print('--------------')


#задание №3--------------
name = input('Введите Ваше имя: ').casefold()
age = int(input('Введите Ваш возраст: '))  

if 0<= age <= 75 and name != 'иван':
    if age >= 16:
        print('Поздравляем вы поступили в ВГУИТ')
    else:
        print(f'Сначала нужно окончить школу!\n\
До окончания школы осталось {16-age} года')
elif name == 'иван':
    print('Тебя зовут Иван') 

print('--------------')


#задание №4 --------------
seconds = int(input('Введите количество секунд: '))
days = seconds // 86400
hours = seconds // 3600
minutes = seconds // 60

print(f'{days}:{hours}:{minutes}:{seconds}')
print('--------------')


# задание №5 --------------
string = input('Введите число: ')
count = 0

for i in range(1,6):
    count += int(string)**i

print(count)
print('--------------')


# задание №6 --------------
x = 1
y = 2
x,y = y,x 

print(x, y)
print('--------------')


# задание №7 --------------
number = int(input('Введите число: '))

if not number % 2:
    print('Четное')
else:
    print('Нечетное')
