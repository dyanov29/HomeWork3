#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = abs(int(input('Введите количество элементов: ')))
List_meaning = input("Введите через пробел элементы списка: ").split()
List_num = list(map(int, List_meaning))
if len(List_num) != N or N == 0:
    print('Заданные элементы не соответсвуют условию')
else:
    X = int(input('Введите число X: '))
    min = abs(X - List_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - List_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {List_num[index]} в списке List наиболее близко по величине к числу {X}')