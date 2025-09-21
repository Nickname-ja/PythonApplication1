import math
# Рыбников Д.А. 91 группа 2 курс
# Некто просто обожает квадраты. Поэтому в его приложении, которое хранит наборы
# целочисленных значений, все они помещаются в квадратные матрицы минимально
# необходимого размера (недостающие числа заполняются нулями). Предусмотреть
# какие-то операции с наборами
#делает квадратную матрицу из набора чисел
def to_square_matrix(seq):
    n = len(seq)
    size = math.ceil(math.sqrt(n))
    matrix = []
    seq = seq + [0] * (size * size - n)
    for i in range(size):
        row = seq[i * size:(i + 1) * size]
        matrix.append(row)
    return matrix
#выводит матрицу на экран
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(f"{elem:4}", end=' ')
        print()
#выводит все наборы
def print_all_sets(sets):
    i = 0;
    if not sets:
        print("Нет наборов.")
        return
    for n in sets:
        i += 1
        print("Набор ", i, ":", sep='')
        print_matrix(n)
#безопасный ввод 1 числа
def safe_inp(massage, lamb):
    if (massage):
        print(massage)
    while True:
        try:
            res = int(input(">").strip())
            if (res > 0 and lamb(res)):
                return res
            else:
                print("Ошибка: номер вне диапазона")
        except ValueError:
            print("Ошибка: введите число.")
#ввод набора чисел из консоли
def inp_num():
    while True:
        raw = input("Введите целые числа\n>").strip()
        parts = raw.split()

        if (all(p.lstrip("+-").isdigit() for p in parts) and parts):
            numbers = [int(p) for p in parts]
            return numbers
        else:
            print("Ошибка ввода.")
#удаляет матрицу по введёному номеру
def del_matrix(sets):
    print_all_sets(sets)
    i = safe_inp("Введите номер набора", lambda x: x < len(sets) + 1) - 1
    sets.pop(i)
#переводит матрицу в набор чисел
def matrix_to_set(matrix):
    s = [x for row in matrix for x in row]
    while s and s[-1] == 0:
        s.pop()
    return s
#объединяет матрицы (исходные матрицы удаляются, получившаяся встаёт на место первой по порядку в программе)
def matrix_concatenation(sets):
    print_all_sets(sets)
    x = safe_inp("Введите номера наборов по очереди", lambda x: x < len(sets) + 1) - 1
    y = safe_inp("", lambda x: x < len(sets) + 1) - 1
    new_set = matrix_to_set(sets[x]) + matrix_to_set(sets[y])
    sets.pop(max(x, y))
    sets[min(x, y)] = to_square_matrix(new_set)
#повторяет набор  введённое количество раз (получившаяся матрица окажется на месте исходной)
def repetition_set(sets):
    print_all_sets(sets)
    i = safe_inp("Введите номер набора", lambda x: x < len(sets) + 1) - 1
    s = matrix_to_set(sets[i])
    n = safe_inp("Ведите кол-во повторений", lambda x: True)
    s = s * (n + 1)
    sets[i] = to_square_matrix(s)

#вычисляет среднее кол-во реальных элементов в наборах
def average_number_of_elements(sets):
    count = 0
    i = 0
    for matrix in sets:
        i += 1
        count += len(matrix_to_set(matrix))
    print("Среднее количество элементов в наборах:", f"{((count * 1.0) / i):.2f}")

# ===========================================================

def main():
    sets = []
    while True:
        #МЕНЮ
        print("1. Добавить набор")
        print("2. Удалить набор")
        print("3. Конкатенация наборов")
        print("4. Повторение набора")
        print("5. Вывод всех наборов")
        print("6. Среднее количество настоящих элементов")
        print("7. Завершить")

        choice = input(">").strip()

        if (choice == "1"):
            sets.append(to_square_matrix(inp_num()))
        elif (choice == "2"):
            del_matrix(sets)
        elif (choice == "3"):
            matrix_concatenation(sets)
        elif (choice == "4"):
            repetition_set(sets)
        elif (choice == "5"):
            print_all_sets(sets)
        elif (choice == "6"):
            average_number_of_elements(sets)
        elif (choice == "7"):
            break
        else:
            print("Ошибка: введите число в диапазоне от 1 до 7")

if __name__ == "__main__":
    main()