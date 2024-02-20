#"Task 1"
# try:
#     pruf = int(input("Введіть номер дня тижня (1-7): "))
#
# except ValueError:
#     print("Помилка: Введіть ціле число від 1 до 7.")
# except KeyError:
#     print("Помилка: Номер дня тижня повинен бути від 1 до 7.")
#
#
# if pruf == 1:
#     print("Monday")
# elif pruf == 2:
#     print("Tuesday")
# elif pruf == 3:
#     print("Wednesday")
# elif pruf == 4:
#     print("Thursday")
# elif pruf == 5:
#     print("Friday")
# elif pruf == 6:
#     print("Saturday")
# elif pruf == 7:
#     print("Sunday")
# else:
#     print("None day")

#
#
# "Task 2"
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#
#     if num1 == num2:
#         print("Числа рівні.")
#     else:
#         print("Числа не рівні. В порядку зростання:", sorted([num1, num2]))
# except ValueError:
#     print("Помилка: Введіть дійсне число.")



# "Task 3"
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     operation = input("Введіть математичну дію (+, -, *, /): ")
#
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             print("Помилка: Ділення на нуль.")
#
#     else:
#         print("Помилка: Невідома математична дія.")
#
#
#     print("Результат: ", result)
#
# except ValueError:
#     print("Помилка: Введіть дійсне число.")



