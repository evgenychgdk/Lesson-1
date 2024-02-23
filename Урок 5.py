from random import randint


# "Task 1"
UK = [randint(-10,10) for num in range(7)]
print(UK)
min_value = [num for num in UK if num < 0]
par_num = [num for num in UK if num % 2 == 0]
nepar_num = [num for num in UK if num % 2 != 0]
ind_num = [num for num in UK[3:6:3]]
dob_num = [num for num in UK]
poz_num = [num for num in UK if num > 0]



print(f'Сума від\'ємних чисел: {sum(min_value)}')
print(f'Сума парних чисел: {sum(par_num)}')
print(f'Сума непарних чисел: {sum(nepar_num)}')
print(f'Сума индекса 3: {sum(ind_num)}')
print(f'Добуток всіх чисел: {UK[0] * UK[1] * UK[2] * UK[3] * UK[4] * UK[5] * UK[6]}')
print(f'Сума між позитивними числами: {sum(poz_num) - (poz_num[0] + poz_num[-1])}')


# "Task 2"
print("             ")
print("Task 2")
print("             ")
lest = UK
print(lest)
par_num = [num for num in lest if num % 2 == 0]
print(f'Парні числа: {par_num}')
nepar_num = [num for num in lest if num % 2 != 0]
print(f'Непарні числа: {nepar_num}')
megav_value = [num for num in lest if num < 0]
print(f'Негатині числа: {megav_value}')
poz_num = [num for num in UK if num > 0]
print(f'Позитивні числа: {poz_num}')






















