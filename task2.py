# Задача 2.
# В результате 10 независимых измерений некоторой величины X, выполненных с
# одинаковой точностью, получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения
# вероятностей, оценить истинное значение величины X при помощи доверительного
# интервала, покрывающего это значение с доверительной вероятностью 0,95.

import numpy as np
import scipy.stats as stats

# Данные задачи
data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n = len(data) # Объем выборки
alpha = 0.05 # Уровень значимости для 95% доверительного интервала

# Среднее значение и стандартное отклонение выборки
mean_X = np.mean(data)
std_dev_X = np.std(data, ddof=1)

# Критическое значение для t-распределения
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)

# Рассчет стандартной ошибки
standard_error = std_dev_X / np.sqrt(n)

# Доверительный интервал
margin_of_error = t_crit * standard_error
confidence_interval = (mean_X - margin_of_error, mean_X + margin_of_error)

print(f"Доверительный интервал: {confidence_interval}")