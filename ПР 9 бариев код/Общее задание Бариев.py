import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Работу выполнил Бариев Энвер БИ
std = float(input("Введите отклонение "))
n = float(input("Введите объём выборки "))
se = std / (np.sqrt(n))

be = float(input("Введите фактическое среднее значение "))
he = float(input("Введите ожидаемое среднее значение "))
test_statistic = (be - he) / se

p = float(input("Введите доверительную вероятность "))
value = norm.ppf(1 - (1 - p) / 2)

print()
print("Входные данные")
print("σ : ", std)
print("n : ", n)
print("p : ", p)
print("X : ", be)
print("a : ", he)

print()
print("Результат работы")
print()
print("Критическое значение выборочного распределения: ", value)
print("Статистика: ", test_statistic)

legend = 'μ: 0, σ: ' + str(std)

if test_statistic > -value and test_statistic < value:
    print("Нулевая гипотеза принимается")
else:
    print("Следует отказаться от нулевой и принять альтернативную гипотезу")

x = np.arange(-5, 5, 0.001)
plt.plot(x, norm.pdf(x, 0, std), color='red', label=legend)
plt.axvline(value, linestyle='--')
plt.axvline(-value, linestyle='--')
plt.legend(title='Parameters')
plt.show()