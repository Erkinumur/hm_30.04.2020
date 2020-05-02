user_list = input('Введите числа через пробел: ').split()
shift = int(input('Укажите сдвиг: '))

if abs(shift) > len(user_list):
    shift = shift % len(user_list)

result = user_list[-shift:]
result.extend(user_list[:-shift])
print(result)