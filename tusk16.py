#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


N = abs(int(input('Введите количество элементов: ')))
List_meaning = input("Введите через пробел элементы списка: ").split()
List_num = list(map(int, List_meaning))
if len(List_num) != N:
    print('Заданные элементы не соответсвуют условию')
else:
    X = int(input('Введите число X: '))
    count = 0
    for i in range(N):
        if List_num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке List {count} раз') 