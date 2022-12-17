'''- Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.'''


number = int(input())
biggest: int = 0
while number > 0:
    part_of_number = number % 10
    if part_of_number > biggest:
        biggest = part_of_number
    number = number // 10
print(biggest)
