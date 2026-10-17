while True:
    try:
        A = int(input("Введите сторону а\n"))  # 1 Сторона
        B = int(input("Введите сторону b\n"))  # 2 Сторона
        C = int(input("Введите сторону c\n"))  # Сторона квадрата
    except ValueError:
        print("Введите только целые числа.")
        continue

    if A <= 0 or B <= 0 or C <= 0:
        print("Все стороны должны быть больше 0")
        continue

    # Считаем площади квадрата и прямоугольника
    square = (C * C)
    pramoyg = (A * B)

    # Количество квадратов в прямоугольнике без остатка и с ним
    сount_sq = (pramoyg // square)
    ostatok = (pramoyg % square)

    # Выводим значения
    print(f"Можно разместить квадратов: {сount_sq}")
    print(f"Остаток: {ostatok}")
    break