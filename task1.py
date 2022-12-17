'''- Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.'''

'''
month_of_year = int(input())
year = ['0', 'yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentyabr', 'octabr', 'noyabr', 'decabr']
if month_of_year >= 1 and month_of_year <= 12:
    print(year[month_of_year])
else:
    print('net takogo month')'''

'''
month_of_year = int(input())
time_of_year = {'zima': ['decabr', 'yanvar', 'fevral'], 'vesna': ['mart', 'aprel', 'may'], 'leto': ['iyun', 'iyul', 'avgust'], 'osen': ['sentyabr', 'octabr', 'noyabr']}
print(year['vesna'])'''

#month_of_year = int(input())
'''
year = ['0', 'yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentyabr', 'octabr', 'noyabr', 'decabr']
time_of_year = {'zima': [year[-1], year[1], year[2]], 'vesna': [year[3], year[4], year[5]], 'leto': [year[6], year[7], year[8]], 'osen': [year[9], year[10], year[11]]}
print(time_of_year['zima'])'''

