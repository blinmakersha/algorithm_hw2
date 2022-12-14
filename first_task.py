# с помощью данной функции, мы находим сколько квадратных подматриц имеют все единицы.
# разделяем задачу на подзадачи, пользуемся динамическим программированием.
# сложность: O(m * n).


# импортируем функцию chain, которая создаёт итератор представляющий единой цепочкой
# элементы указанных объектов.
from itertools import chain     

trial_matrix = [
                [0,1,1,1],
                [1,1,1,1],
                [0,1,1,1]
                ]

def countSquares(matrix) -> int:
        
    # DP[y][x] обозначает наибольшую длину ребра квадрата,
    # нижняя правая точка которого равна [y][x]
    dp = matrix
        
    height, weight = len(matrix), len(matrix[0])
        
    # пройдемся по каждой ячейке в матрице
    for y in range(1, height):
        for x in range(1, weight):

            # воспользуемся условным оператором. матрица [y][x] должна быть равна 1,
            # чтобы квадрат мог принимать текущую ячейку.
            if matrix[y][x]:
                    
                # обновляем наибольшую длину ребра квадрата, нижняя точка которого
                # равна [y][x]
                dp[y][x] = 1 + min(dp[y][x-1],dp[y-1][x-1],dp[y-1][x])
    
    # возвращаем сумму всех чисел в новой таблице,
    # чтобы выяснить необходимый в задаче результат
    return sum(chain(*dp))

print(countSquares(trial_matrix))
