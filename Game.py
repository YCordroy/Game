import random as r

random_num = r.randrange(1, 101)
loss = 7
message = "Введите число от 1 до 100: "

print(f"У вас {loss} попыток")

user_num = input(message)

while not user_num.isdigit() or int(user_num) not in range(1, 101):
    print("Некоректное значение.")
    user_num = input(message)

user_num = int(user_num)

while user_num != random_num and loss > 0:
    if random_num < user_num:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
    loss -= 1
    print(f"У вас {loss} попыток")
    if loss == 0:
        break
    user_num = input(message)
    while not user_num.isdigit() or int(user_num) not in range(1, 101):
        print("Некоректное значение.")
        user_num = input(message)
    user_num = int(user_num)

print("Угадал" if user_num == random_num else "Вы проиграли")