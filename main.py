import math

while True:
    print("\nКалькулятор с расширенными функциями")
    print("Доступные операции: +, -, *, /, ^ (степень), % (остаток), sqrt (квадратный корень)")
    print("Введите 'выход' чтобы завершить")

    op = input("Операция (+, -, *, /, ^, %, sqrt): ")
    if op.lower() == 'выход':
        break

    if op == 'sqrt':
        a = input("Введите число: ")
        if a.lower() == 'выход':
            break
        try:
            a = float(a)
            if a >= 0:
                print(f"Результат: {math.sqrt(a)}")
            else:
                print("Ошибка: нельзя извлечь корень из отрицательного числа.")
        except ValueError:
            print("Ошибка: введите числовое значение.")
    else:
        a = input("Введите первое число: ")
        if a.lower() == 'выход':
            break
        b = input("Введите второе число: ")
        if b.lower() == 'выход':
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
            elif op == '^':
                print(f"Результат: {a ** b}")
            elif op == '%':
                if b != 0:
                    print(f"Результат: {a % b}")
                else:
                    print("Ошибка: деление на ноль!")
            else:
                print("Неизвестная операция.")
        except ValueError:
            print("Ошибка: введите числовые значения.")
