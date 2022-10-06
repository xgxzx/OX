def print_deck():
    print(f'{table[0][0]} {table[0][1]} {table[0][2]} {table[0][3]}\n'
          f'{table[1][0]} {table[1][1]} {table[1][2]} {table[1][3]}\n'
          f'{table[2][0]} {table[2][1]} {table[2][2]} {table[2][3]}\n'
          f'{table[3][0]} {table[3][1]} {table[3][2]} {table[3][3]}\n')


def winner_check(*args, **kwargs):
    global game_winner
    global count
    if table[1][1] == table[1][2] == table[1][3] != '-'\
            or table[2][1] == table[2][2] == table[2][3] != '-'\
            or table[3][1] == table[3][2] == table[3][3] != '-'\
            or table[1][1] == table[2][1] == table[3][1] != '-'\
            or table[1][2] == table[2][2] == table[3][2] != '-'\
            or table[1][3] == table[2][3] == table[3][3] != '-'\
            or table[1][1] == table[2][2] == table[3][3] != '-'\
            or table[3][1] == table[2][2] == table[1][3] != '-':
        if count % 2 == 0:
            game_winner = 'Победа за крестиками.'
        else:
            game_winner = 'Победа за ноликами.'
    else:
        if count == 9:
            game_winner = 'Ого! Да тут ничья!'


def move_check(*args, **kwargs):
    global table
    global count
    while True:
        line = input("Введите координаты строки: ")
        try:
            line = int(line)
            if 0 < line < 4:
                break
            else:
                print('Неверное число.')
        except:
            print('Ошибка ввода.')
    while True:
        column = input("Введите координаты столбца: ")
        try:
            column = int(column)
            if 0 < column < 4:
                break
            else:
                print('Неверное число.')
        except:
            print('Ошибка ввода.')
    if table[line][column] == "-":
        if count % 2 != 0:
            table[line][column] = 'X'
            count += 1
            winner_check()
        else:
            table[line][column] = 'O'
            count += 1
            winner_check()
    else:
        print("")
        print("Ячейка занята.")


table = [[" ", 1, 2, 3], [1, "-", "-", "-"], [2, "-", "-", "-"], [3, "-", "-", "-"]]
count = 0
game_winner = 0

while game_winner == 0:
    print_deck()
    move_check()
else:
    print_deck()
    print(f"Игра окончена! {game_winner}")
