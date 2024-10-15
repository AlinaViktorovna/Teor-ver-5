# Задача 3.
# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 Рост матерей 178, 165,
# 165, 173, 168, 155, 160, 164, 178, 175 Используя эти данные построить 95%
# доверительный интервал для разности среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats

# Данные задачи
mothers_height = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
daughters_height = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]

# Объем выборок
n1 = len(mothers_height)
n2 = len(daughters_height)

# Средние значения и дисперсии
mean_mothers = np.mean(mothers_height)
mean_daughters = np.mean(daughters_height)
var_mothers = np.var(mothers_height, ddof=1)
var_daughters = np.var(daughters_height, ddof=1)

# Объединённая дисперсия
pooled_variance = ((n1 - 1) * var_mothers + (n2 - 1) * var_daughters) / (n1 + n2 - 2)

# Критическое значение для t-распределения
alpha = 0.05
t_crit = stats.t.ppf(1 - alpha / 2, df=n1 + n2 - 2)

# Рассчет стандартной ошибки разности средних
standard_error_diff = np.sqrt(pooled_variance * (1 / n1 + 1 / n2))

# Доверительный интервал
margin_of_error = t_crit * standard_error_diff
confidence_interval = (mean_mothers - mean_daughters - margin_of_error, mean_mothers - mean_daughters + margin_of_error)

print(f"Доверительный интервал для разности средних: {confidence_interval}")