import random
from decouple import config


def play_game():
    my_money = int(config('MY_MONEY'))

    while True:
        win_number = random.randint(1, 30)
        print(f"Ваш баланс: {my_money}")
        bet = int(input("Сделайте ставку: "))
        if bet > my_money:
            print("У вас недостаточно средств")
            continue
        if bet == 0:
            print("Ставка не может быть равна нулю")
            continue
        my_money -= bet
        number = int(input("Выберите число от 1 до 30: "))
        if number == win_number:
            my_money += bet * 2
            print("Поздравляем, вы выиграли!")
        else:
            print("К сожалению, вы проиграли")
        again = input("Хотите сыграть еще раз? (да/нет) ")
        if again.lower() == 'нет':
            break
    print(f"Игра окончена. Ваш баланс: {my_money}")
    if my_money > int(config('MY_MONEY')):
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")
