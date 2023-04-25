import algorithms as sb
import file_manager as fm

# Пример
# Вводим стартовые значения и интервалы - получаем матрицу P
p = sb.get_p_matrix_sugar(size=8, has_breaking=True, file_writing=True,
                          min_start_sugar=1, max_start_sugar=1,
                          min_degradation=0.7, max_degradation=0.7)

# Вывод матрицы P
for i in range(len(p)):
    print(p[i])

p = sb.get_p_matrix_sugar(size=8, has_breaking=False, file_writing=False,
                          min_start_sugar=1, max_start_sugar=1,
                          min_degradation=0.7, max_degradation=0.7)
print('\n')
# Вывод матрицы P
for i in range(len(p)):
    print(p[i])

str(.5)
file = open(file='result.txt', mode='w', encoding='utf-8')
for i in range(len(p)):
    _str = p[i]
    file.write('\n')
    for j in range(len(_str)):
        file.write("{:.4}".format(p[i][j]))
        file.write(' ')



# Используем сгенерированную матрицу P и передаем ее в функции расчета

# Венгерский минимальный
res, indices = sb.hungarian_min(p)
print("hungarian_min")
print(res)
print(indices)
fm.write_algorithm_res("Венгерский минимальный", res, indices)

# Венгерский максимальный
res, indices = sb.hungarian_max(p)
print("hungarian_max")
print(res)
print(indices)

# Жадный алгоритм
res, indices = sb.greedy(p)
print("greedy")
print(res)
print(indices)

# Бережливый алгоритм
res, indices = sb.saving(p)
print("saving")
print(res)
print(indices)

# Бережливо-жадный алгоритм
res, indices = sb.saving_greedy(p, 1)
print("saving_greedy")
print(res)
print(indices)

# Жадно-бережливый алгоритм
res, indices = sb.greedy_saving(p, 1)
print("greedy_saving")
print(res)
print(indices)






