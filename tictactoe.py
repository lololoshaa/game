field = [["-"] * 3 for i in range(3)]    # создание игрового поля

def show(field):                   # показывает поле игрокам, но немного в другом виде
    print("  0 1 2")
    for i, row in enumerate(field):
        print(i, " ".join(row))

winning = [[(0,0),(0,1),(0,2)],    # выигрышные "позиции"
[(1,0),(1,1),(1,2)],
[(2,0),(2,1),(2,2)],
[(0,0),(1,0),(2,0)],
[(0,1),(1,1),(2,1)],
[(0,2),(1,2),(2,2)],
[(0,0),(1,1),(2,2)],
[(2,0),(1,1),(0,2)]]

def check_field(field):          # проверка игрового поля
    for line in winning:
        a, b, c = line
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != "-":
            return field[a[0]][a[1]]
    if any("-" in row for row in field):
        return None
    return "draw"

def coord(question):            # проверка правильности введения
    while True:
        text = input(question)
        if not text.isdigit():
            print("Неверно, введите число от 0-2: ")
            continue
        number = int(text)
        if not (0 <= number <= 2):
            print("Число должно быть от 0-2, введите число: ")
            continue
        return number

def motion(field, player):      # получение координат от игрока
    while True:
        row = coord(f"Ход игрока {player}, выберите строку (0-2): ")
        col = coord(f"Выберите столбец (0-2): ")
        if field[row][col] != "-":
            print("Эта ячейка уже занята. Выберите другую")
            continue
        return row, col

def game():              # основной ход игры
    player = "X"
    while True:
        show(field)
        row, col = motion(field, player)
        field[row][col] = player
        result = check_field(field)
        if result == "draw":
            show(field)
            print("Ничья. Игра окончена")
            break
        elif result is not None:
            show(field)
            print(f"Победил игрок {player}, игра окончена")
            break
        player = "O" if player == "X" else "X"
game()