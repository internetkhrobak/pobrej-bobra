while True:
    print("\nПростой калькулятор")
    print("Операции: +, -, *, /")
    print("Введите 'выход' чтобы завершить")

    a = input("Введите первое число: ")
    if a.lower() == 'выход':
        break

    op = input("Введите операцию (+, -, *, /): ")
    if op.lower() == 'выход':
        break

    b = input("Введите второе число: ")
    if b.lower() == '':
        break

    try:
        a = float(a)
        b = float(b)

        if op == '+':
            print(f"Результат: {a + b}")
        elif op == '-':
            print(f"Результат: {a - b}")
        elif op == '*':
            print(f"Результат: {a * b}")
        elif op == '/':
            if b != 0:
                print(f"Результат: {a / b}")
            else:
                print("Ошибка: деление на ноль!")
        else:
            print("Неизвестная операция.")
    except ValueError:
        print("Ошибка: введите числовые значения.")
