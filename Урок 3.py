# #
# #
# pruf = int(input("Введіть число:"))
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
pruf1 = int(input("Enter first number:"))
pruf2 = int(input("Enter second number:"))

if pruf1 == pruf2:
    print("Numberі are equal to")
elif pruf1 > pruf2:
    print(pruf2,',',pruf1)
elif pruf1 < pruf2:
    print(pruf1,",",pruf2)
else:
    print("WTF")
