# Гра Камінь-ножиці-папір
# Граємо проти ПК, поки хтось не набере певну кількість балів: 3, 5 чи то більше.
# Умовно позначаємо:
# камінь = 1
# ножиці = 2
# папір = 3
# ПЕРШИЙ ГЕНЕРУЄМО випадковий ход ПК, 
# ПОТІМ запитуємо який ХІД ГРАВЦЯ
# Порівнюємо значення:
#  нічія: (1 І 1) АБО (2 І 2) АБО (3 І 3)
# переміг ПК: (1 І 2) АБО (2 І 3) АБО (3 І 1)
# переміг ГРАВЕЦЬ: (1 І 3) АБО (2 І 1) АБО (3 І 2)
# Додатково коли генеруємо хід ПК, можно імітувати ніби ПК думає роблячі різний час затримки проекту.
import random
import time

moves = {1: "Камінь", 2: "Ножиці", 3: "Папір"}

def get_computer_move():
    print("Комп'ютер думає...", end='', flush=True)
    time.sleep(random.uniform(0.5, 1.5)) 
    move = random.randint(1, 3)
    return move

def get_player_move():
    while True:
        try:
            choice = int(input("Ваш хід (1 = Камінь, 2 = Ножиці, 3 = Папір): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Введіть число від 1 до 3.")

def winner(player, computer):
    if player == computer:
        return "Нічия"
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        return "Гравець"
    else:
        return "Комп'ютер"

def play_game(target_score):
    player_score = 0
    computer_score = 0

    while player_score < target_score and computer_score < target_score:
        computer_move = get_computer_move()
        player_move = get_player_move()

        result = winner(player_move, computer_move)
        if result == "Гравець":
            player_score += 1
            print("Ви перемогли в цьому раунді!")
        elif result == "Комп'ютер":
            computer_score += 1
            print("Комп'ютер переміг в цьому раунді.")
        else:
            print("Нічия!")

        print(f"Рахунок: Гравець {player_score} - {computer_score} Комп'ютер\n")

    if player_score > computer_score:
        print("Вітаємо! Ви перемогли гру!")
    else:
        print("Комп'ютер переміг гру. Спробуйте ще раз!")

if __name__ == "__main__":
    print("Ласкаво просимо до гри 'Камінь-ножиці-папір'!")
    target_score = int(input("До скількох балів граємо? Введіть число: "))
    play_game(target_score)