# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# ________________________________________________________________

# password, secondpassword = input(), input()
# if password == secondpassword:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# _________________________________________________________________

# num = int(input())                                                                                            
# if num % 2 == 0:                                                                                  # if - если
#     print('Четное')                                                                                                это условные операторы отделяются блоком кода у которого отступ 4 символа (обязательно)
# else:                                                                                             # else - ещё
#     print('Нечетное')                                                                             # Двоеточие (:) в конце строки с инструкцией if, else сообщает интерпретатору Python, что дальше находится блок команд
                                                                                                    # == Для проверки двух элементов на равенство Python использует удвоенный знак равно
# ___________________________________________________________________                               # не путать с = (присваивание значения)

# num = int(input())
# a = num // 1000 
# b = (num // 100) % 10
# c = (num // 10) % 10
# d = (num % 100) % 10
# if a + d == b - c:
#     print('ДА')
# else:
#     print('НЕТ')

# _________________________________________________________________

# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')
    
# ________________________________________________________________

# a, b, c = int(input()), int(input()), int(input())
# if (b - a) + b == c:
#     print('YES')
# else:
#     print('NO')
# ________________________________________________________________

# a, b = int(input()), int(input())
# if a < b:
#     print(a)
# else:
#     print(b)
# ______________________________________________________________

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     a = b
# if a > c:
#     a = c
# if a > d:
#     a = d
# print(a)
# ______________________________________________________________________

# ago = int(input())
# if ago <= 13:
#     print('детство')
# if 14 <= ago <= 24:
#     print('молодость')
# if 25 <= ago <=59:
#     print('зрелость')
# if ago >= 60:
#     print('старость')

# _________________________________________________________________

# a, b, c = int(input()), int(input()), int(input())
# if a <= 0:
#     a = 0
# if b <= 0:
#     b = 0
# if c <= 0:
#     c = 0
# print(a + b + c)
#_________________________________________________________________

# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# city = input('В каком городе вы живете?: ')
# if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):                      # Логические операторы and(и), or(или), not(меняет наоборот)
#     print('Доступ разрешен.')                                                                         # приоритет выполнения: в первую очередь выполняется логическое отрицание not,
# else:                                                                                                 # далее выполняется логическое умножение and, далее выполняется логическое сложение or
#     print('Доступ запрещен.')                                                                         # Для явного указания порядка выполнения условных операторов используют скобки.

#__________________________________________________________________________
# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)          # ОТСТУП :) Блок команд закончен.
# print(p)

# ______________________________________________________________________

# a = int(input())
# if -1 < a < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
# ______________________________________________________________________

# a = int(input())
# if a <= -3 or a >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# _____________________________________________________________________

# a = int(input())
# if -30 < a <= -2 or 7 < a <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
#______________________________________________________________________

# a = int(input())
# if (1000 <= a <= 9999) and (a % 7 == 0 or a % 17 == 0):
#     print('YES')
# else:
#     print('NO')
# _____________________________________________________________________

# a, b, c = int(input()), int(input()), int(input())
# if ((a < (b + c)) and ((b + a) > c) and ((c + a) > b )):
#     print('YES')
# else:
#     print('NO')

# _____________________________________________________________________

# a = int(input())
# if a % 4 == 0 and a % 100 > 0 or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# _____________________________________________________________________

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a != c and b == d) or (b != d and a == c): 
#     print('YES')
# else:
#     print('NO') 
# _____________________________________________________________________

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (-1 <= c - a <= 1) and (-1 <= d - b <= 1):
#     print('YES')
# else:
#     print('NO')
# _____________________________________________________________________


# grade = int(input('какой у вас балл:'))
# if grade >= 90:                   
#     print(5)
# elif grade >= 80:
#     print(4)
# elif grade >= 70:                         # elif каскадный условный оператор (применим когда нужно несколько условий, Заключительный блок else в операторе if-elif-else необязательный)
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)
# _________________________________________________________________

# a, b = int(input()), int(input())
# if a > b:
#     print('NO')
# elif b > a:
#     print('YES')
# else:
#     print("Don't know")
#__________________________________________________________________

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a != b and a != c and c != b:
#     print('Разносторонний')
# else:
#     print('Равнобедренный')

# ________________________________________________________________

# a, b, c = int(input()), int(input()), int(input())
# if a < b < c or c < b < a:
#     print(b)
# elif b < a < c or c < a < b:
#     print(a)
# else:
#     print(c)
# _______________________________________________________________

# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print(31)
# elif a == 2:
#     print(28)
# else:
#     print(30)

# _______________________________________________________________

# a = int(input())
# if a < 60:
#     print('Легкий вес')
# elif 60 <= a < 64:
#     print('Первый полусредний вес')
# elif 64 <= a < 69:
#     print('Полусредний вес')
# ______________________________________________________________

# a, b, c = int(input()), int(input()), input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')                                          # КАЛЬКУЛЯТОР :)
#     else:
#         print(a / b)
# elif c == '*':
#     print(a * b)
# else:
#     print('Неверная операция')
# ______________________________________________________________

# a, b = input(), input()
# if (a == 'красный' and b == 'синий') or (a =='синий' and b == 'красный'):
#     print('фиолетовый')
# elif (a == 'красный' and b == 'желтый') or (a =='желтый' and b == 'красный'):
#     print('оранжевый')
# elif (a == 'синий' and b == 'желтый') or (a =='желтый' and b == 'синий'):                        # СМЕСЬ ЦВЕТОВ
#     print('зеленый')
# elif a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'синий' and b == 'синий':
#     print('синий')
# elif a == 'желтый' and b == 'желтый':
#     print('желтый')
# else:
#     print('ошибка цвета')
# _________________________________________________________________

# roll = int(input())
# if (1 <= roll <= 10) and roll % 2 == 0:
#     print('черный')
# elif (1 <= roll <= 10) and roll % 2 != 0:
#     print('красный')
# elif (11 <= roll <= 18) and roll % 2 == 0:
#     print('красный')
# elif (11 <= roll <= 18) and roll % 2 != 0:
#     print('черный')
# elif (19 <= roll <= 28) and roll % 2 == 0:                                # ЛАС ВЕГАС КАЗИНО
#     print('черный')
# elif (19 <= roll <= 28) and roll % 2 != 0:
#     print('красный')
# elif (29 <= roll <= 36) and roll % 2 == 0:
#     print('красный')
# elif (29 <= roll <= 36) and roll % 2 != 0:
#     print('черный')
# elif roll == 0:
#     print('зеленый')
# else:
#     print('ошибка ввода')

# _______________________________________________________________

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < c and b > d:
#     print(c, d)
# elif a > c and b < d:
#     print(a, b)
# elif a < c and b < d:
#     print(c, b)
# elif c < a and d < b:
#     print(a, d)
# elif a == c and b == d:
#     print(a, b)
# elif b == c:
#     print(b)
# elif d == a:
#     print(d)
# elif a == c and b < d:
#     print(a, b)
# elif c < a and b == d:
#     print(a, b)
# elif a < c and b == d:
#     print(c, d)
# elif a == c and d < b:
#     print(c, d)
# else:
#     print('пустое множество')

# __________________________________________________________________

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

# if a2 < a1:
#     if b2 < a1:
#         print('пустое множество')
#     elif b2 == a1:
#         print(b2)
#     elif a1 < b2 <= b1:
#         print(a1, b2)
#     elif b2 > b1:
#         print(a1, b1)
# elif a2 == a1:
#     if b2 <= b1:
#         print(a2, b2)
#     else:
#         print(a2, b1)
# elif a2 < b1:
#     if b2 <= b1:
#         print(a2, b2)
#     else:
#         print(a2, b1)
# elif a2 == b1:
#     print(a2)
# else:
#     print('пустое множество')
# _______________________________________________________________

# a = int(input())
# if a % 100 == 0 or a % 1000 == 0:
#     print('YES')
# else:
#     print('NO')

# ______________________________________________________________

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a + b + c + d) % 2 == 0:
#     print('YES')
# else:
#     print('NO')
# ______________________________________________________________

# a, b = int(input()), input()
# if 10 <= a <= 15 and b == 'f':
#     print('YES')
# else:
#     print('NO')

# _____________________________________________________________

# a = int(input())
# if a == 1:
#     print('I')
# else:
#     if a == 2:
#         print('II')
#     else:
#         if a == 3:
#             print('III')
#         else:
#             if a == 4:
#                 print('IV')
#             else:
#                 if a == 5:
#                     print('V')
#                 else:
#                     if a == 6:
#                         print('VI')
#                     else: 
#                         if a == 7:
#                             print('VII')
#                         else:
#                             if a == 8:
#                                 print('VIII')
#                             else:
#                                 if a == 9:
#                                     print('IX')
#                                 else:
#                                     if a == 10:
#                                         print('X')
#                                     else:
#                                         print('ошибка')
# ______________________________________________________________________

# a = int(input())
# if (a % 2 != 0) or ((6 <= a <= 20) and (a % 2 == 0)):
#     print('YES')
# else:
#     print('NO')

# __________________________________________________________

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a1 != a2 and b1 != b2):
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if ((a1 + b1) - (a2 + b2) == 2) or ((a1 + b1) - (a2 + b2) == -2) or ((a1 + b1) - (a2 + b2) == 0) or (a1 != a2 and b1 != b2):
#     print('YES')
# else:
#     print('NO')
        
        
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a1 + b1) == (a2 + b2) or (a1- a2) == (b1 - b2):
#     print('YES')                                                                    # ход слона (правильное решение)
# else:
#     print('NO')
        
# _________________________________________________________________


# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (((a1 - a2) == 1 or (a1 - a2) == - 1) and ((b1 - b2) == 2 or (b1 - b2) == -2)) or (((a1 - a2) == 2 or (a1 - a2) == - 2) and ((b1 - b2) == 1 or (b1 - b2) == -1)):
#     print('YES')
# else:                                                     # ШАХМАТЫ ХОД КОНЯ
#     print('NO')
# ____________________________________________________________________________________

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if ((a1 + b1) == (a2 + b2) or (a1- a2) == (b1 - b2)) or ((a1 != a2 and b1 == b2) or (a1 == a2 and b1 != b2)) or ((-1 <= a2 - a1 <= 1) and (-1 <= b2 - b1 <= 1)):
#     print('YES')
# else:                                                       # ШАХМАТЫ ВСЕ ХОДЫ ФИГУР В ОДНОЙ ЗАДАЧЕ
#     print('NO')                                                            
# ______________________________________________________________________________________












    





