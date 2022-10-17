def time(num):
    seconds = ((((num % 2592000) % 86400) % 3600) % 60)
    minute = (((num % 2592000) % 86400) % 3600) // 60
    hour = ((num % 2592000) % 86400) // 3600
    day = (num % 2592000) // 86400
    month = num // 2592000
    print(month, 'мес.', day, 'дн.', hour, 'час.', minute, 'мин.', seconds, 'сек.')

try:
    num = int(input('Введите любое целое число: '))
    time(num)
except:
    print('Ошибка, вы ввелdfgи неверное число!')