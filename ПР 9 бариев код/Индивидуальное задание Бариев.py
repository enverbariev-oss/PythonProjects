import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
#Работу выполнил Бариев Энвер БИ
a = float(input("Введите утвержденный средний вес (a): "))
p = float(input("Введите доверительную вероятность (p): "))

data_input = input("Введите веса всех пачек через пробел: ")
weights = [float(x) for x in data_input.split()]

n = len(weights)
x_mean = np.mean(weights)
std_dev = np.std(weights, ddof=1)
se = std_dev / np.sqrt(n)

t_statistic = (x_mean - a) / se

df = n - 1
alpha = 1 - p
t_critical = t.ppf(1 - alpha / 2, df)

print("\n" + "="*30)
print(f"Объем выборки (n): {n}")
print(f"Среднее по выборке (X_ср): {x_mean:.2f}")
print(f"Стандартное отклонение (s): {std_dev:.4f}")
print(f"Статистика t: {t_statistic:.10f}")
print(f"Критические границы: [{-t_critical:.3f}; {t_critical:.3f}]")
print("="*30)

print("\nИТОГ:")
if -t_critical < t_statistic < t_critical:
    print(">>> Нулевая гипотеза принимается.")
    print(">>> Производитель не врет, отклонения являются случайными.")
else:
    print(">>> Нулевая гипотеза отвергается.")
    print(">>> Отклонение существенно, утверждение производителя не подтверждается.")

x = np.linspace(-5, 5, 500)
y = t.pdf(x, df)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label=f'Распределение Стьюдента (df={df})', color='royalblue', lw=2)
plt.fill_between(x, y, where=(x > t_critical) | (x < -t_critical), color='red', alpha=0.3, label='Область отвержения H0')
plt.axvline(t_statistic, color='green', linestyle='-', label=f'Ваша t-статистика ({t_statistic:.2f})')

plt.title("Визуализация проверки гипотезы (Задание 5.2)")
plt.xlabel("t-значение")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.grid(True, alpha=0.2)
plt.show()