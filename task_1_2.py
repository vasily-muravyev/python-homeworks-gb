# Задание 2

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Please enter amount of seconds:\n>>> '))

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

hours = seconds // SECONDS_IN_HOUR

seconds = seconds % SECONDS_IN_HOUR
minutes = seconds // SECONDS_IN_MINUTE

seconds = seconds % SECONDS_IN_MINUTE

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
