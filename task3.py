'''
- Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

number_1 = input()
number_2: int = number_1 + number_1
number_3: int = number_1 + number_1 +  number_1
sum_number: int = int(number_1) + int(number_2) + int(number_3)
print(sum_number)
