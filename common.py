# total_cars = 100
# sold_cars = 20
# total_cars -= sold_cars
# print(total_cars)
from unittest import case

# point = (2, 5)
# match point:
#     case (x, y):
#         print(f'({x}, {y}) is in plane')
#     case (x, y, z):
#         print(f'({x}, {y}, {z}) is in space')

# auth = [
#     {"username": "admin", "password": "1234"},
#     {"email": "user@gmail.com", "token": "3456"},
#     {"email": "test@test.com", "token": "ABC"},
#     {"username": "admin", "password: 1234}
# ]
#
# for auth in auths:
#     print(auth)
#     match auth:
#         case {"username": str(username), "password": str(password)}:
#             print("Authenticated")
#             print(f'{username}: {password}')

# def create_user():
#     name = 'Alex'
#     age = 20
#     user_data = [name, age]
#     return user_data
#
# my_user = create_user()
# print(my_user)

MAX_GREETS = 1
num_greets = 0
want_greet = 'Да'

while want_greet == 'Да':
    print('Привет, как дела?')
    num_greets +=1
    want_greet = input('Хотите еще одно приветствие? [Да/Нет]')

    if num_greets == MAX_GREETS:
        print('Достигнуто максимальное количество приветствий.')
        break

else:
    print('Вы отказались от приветствия.')
print('Хорошего дня!')