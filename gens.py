from random import uniform
# Отсюда ничего брать не надо, все нужные функции находятся в algorithms.py

def rand_vector(n: int, _min: float, _max: float):
    """Возвращает список размера n со случайными значениями от _min до _max."""
    result = []
    for i in range(n):
        result.append(uniform(_min, _max))
    return result


def rand_matrix(_str: int, _col: int, _min: float, _max: float):
    """Возвращает двумерный список размера (_str)x(_col) со случайными значениями от _min до _max."""
    result = []
    for i in range(_str):
        _str = []
        for j in range(_col):
            _str.append(uniform(_min, _max))
        result.append(_str)
    return result



def get_p_matrix(a_vector, b_matrix, has_breaking: bool):
    """Возвращает матрицу P для решения задачи оптимизации (Элементы в ней не могут быть больше 1).
    a_vector - вектор стартовых значений сахаристости размера n,
    b_matrix - матрица деградации размера (n)x(n+1)
    has_breaking - были ли поломки оборудования."""

    n = len(a_vector)
    result = []

    break_1_day = 1
    break_2_day = n//2 + 1

    for i in range(n):
        _str = [a_vector[i]]
        day = 0
        work_day = 0
        while work_day < n-1:
            res = _str[work_day] * b_matrix[i][day]

            if day == break_1_day and has_breaking:
                res *= b_matrix[i][day]
                day += 1

            if day == break_2_day and has_breaking:
                res *= b_matrix[i][day]
                day += 1

            _str.append(res)
            work_day += 1
            day += 1

        result.append(_str)

    return result
