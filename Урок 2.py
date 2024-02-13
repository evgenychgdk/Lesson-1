#
# numbers = input('Введыть трьох значне число: ')
#
#
# if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
#     print('Max:', numbers[0])
# elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
#     print('Max: ', numbers[1])
# elif numbers[2] > numbers[0] and numbers[2] > numbers[1]:
#     print('Max: ', numbers[2])
# else:
#     print('Numbers =')
#
# if numbers[0] <= numbers[1] and numbers[0] <= numbers[2]:
#     print('Min:', numbers[0])
# elif numbers[1] <= numbers[0] and numbers[1] <= numbers[2]:
#     print('Min: ', numbers[1])
# elif numbers[2] <= numbers[0] and numbers[2] <= numbers[1]:
#     print('Min: ', numbers[2])
# else:
#     print('Вони рівні')
# sum_numlbers = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
# print('Середнє арифметичне: ', int(sum_numlbers) // 3)


UK1 = int(input("Введіть метри:"))
UK2 = input("Одиниці виміру:")

if UK2 == "милі":
    print(UK1 * 0.000621371)
elif UK2 == "дюйми":
    print(UK1 * 39.3701)
elif UK2 == "ярди":
    print(UK1 * 1.093613888889)
else:
    print('Программа не обчислюэ такы одиницы')







