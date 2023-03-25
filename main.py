import sugarbeet as sb

# Пример
# Вводим стартовые значения и интервалы - получаем матрицу P
p = sb.gen_p_matrix(size=5, sugar_divider=2,
                    min_start_sugar=0.8, max_start_sugar=1,
                    min_sugaring=1.1, max_sugaring=1.5,
                    min_degradation=0.7, max_degradation=0.9)

# Вывод матрицы P
for i in range(len(p)):
    print(p[i])

# Используем сгенерированную матрицу P и передаем ее в функции расчета

# Венгерский минимальный
res, indices = sb.hungarian_min(p)
print("hungarian_min")
print(res)
print(indices)

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






