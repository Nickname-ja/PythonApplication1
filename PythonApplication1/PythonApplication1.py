import math
# �������� �.�. 91 ������ 2 ����
# ����� ������ ������� ��������. ������� � ��� ����������, ������� ������ ������
# ������������� ��������, ��� ��� ���������� � ���������� ������� ����������
# ������������ ������� (����������� ����� ����������� ������). �������������
# �����-�� �������� � ��������
#������ ���������� ������� �� ������ �����
def to_square_matrix(seq):
    n = len(seq)
    size = math.ceil(math.sqrt(n))
    matrix = []
    seq = seq + [0] * (size * size - n)
    for i in range(size):
        row = seq[i * size:(i + 1) * size]
        matrix.append(row)
    return matrix
#������� ������� �� �����
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(f"{elem:4}", end=' ')
        print()
#������� ��� ������
def print_all_sets(sets):
    i = 0;
    if not sets:
        print("��� �������.")
        return
    for n in sets:
        i += 1
        print("����� ", i, ":", sep='')
        print_matrix(n)
#���������� ���� 1 �����
def safe_inp(massage, lamb):
    if (massage):
        print(massage)
    while True:
        try:
            res = int(input(">").strip())
            if (res > 0 and lamb(res)):
                return res
            else:
                print("������: ����� ��� ���������")
        except ValueError:
            print("������: ������� �����.")
#���� ������ ����� �� �������
def inp_num():
    while True:
        raw = input("������� ����� �����\n>").strip()
        parts = raw.split()

        if (all(p.lstrip("+-").isdigit() for p in parts) and parts):
            numbers = [int(p) for p in parts]
            return numbers
        else:
            print("������ �����.")
#������� ������� �� �������� ������
def del_matrix(sets):
    print_all_sets(sets)
    i = safe_inp("������� ����� ������", lambda x: x < len(sets) + 1) - 1
    sets.pop(i)
#��������� ������� � ����� �����
def matrix_to_set(matrix):
    s = [x for row in matrix for x in row]
    while s and s[-1] == 0:
        s.pop()
    return s
#���������� ������� (�������� ������� ���������, ������������ ����� �� ����� ������ �� ������� � ���������)
def matrix_concatenation(sets):
    print_all_sets(sets)
    x = safe_inp("������� ������ ������� �� �������", lambda x: x < len(sets) + 1) - 1
    y = safe_inp("", lambda x: x < len(sets) + 1) - 1
    new_set = matrix_to_set(sets[x]) + matrix_to_set(sets[y])
    sets.pop(max(x, y))
    sets[min(x, y)] = to_square_matrix(new_set)
#��������� �����  �������� ���������� ��� (������������ ������� �������� �� ����� ��������)
def repetition_set(sets):
    print_all_sets(sets)
    i = safe_inp("������� ����� ������", lambda x: x < len(sets) + 1) - 1
    s = matrix_to_set(sets[i])
    n = safe_inp("������ ���-�� ����������", lambda x: True)
    s = s * (n + 1)
    sets[i] = to_square_matrix(s)

#��������� ������� ���-�� �������� ��������� � �������
def average_number_of_elements(sets):
    count = 0
    i = 0
    for matrix in sets:
        i += 1
        count += len(matrix_to_set(matrix))
    print("������� ���������� ��������� � �������:", f"{((count * 1.0) / i):.2f}")

# ===========================================================

def main():
    sets = []
    while True:
        #����
        print("1. �������� �����")
        print("2. ������� �����")
        print("3. ������������ �������")
        print("4. ���������� ������")
        print("5. ����� ���� �������")
        print("6. ������� ���������� ��������� ���������")
        print("7. ���������")

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
            print("������: ������� ����� � ��������� �� 1 �� 7")

if __name__ == "__main__":
    main()