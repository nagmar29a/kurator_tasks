'''- Пользователь вводит время в секундах. 
 Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
 Используйте форматирование строк.'''

second = int(input())
hour: int = second // 60 // 60 % 24
hour = str(hour)
hour: str = hour.rjust(2, '0')
minutes_output_1: int = (second // 60 % 60) // 10
minutes_output_2: int = (second // 60 % 60) % 10
seconds_output_1: int = (second % 60) // 10
seconds_output_2: int = (second % 60) % 10

print(f'Точное время: {hour}:{minutes_output_1}{minutes_output_2}:{seconds_output_1}{seconds_output_2}')
