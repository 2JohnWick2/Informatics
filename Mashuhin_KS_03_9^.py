'''
1. при различных значениях α и β.

Для каждой задачи необходимо:

Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), график каждой функции должен быть одного цвета для одного значения α и β.
Подписать оси и заголовок
Создать легенду
Сохранить изображение в svg файл
Построить в общих осях графики для:
α=1,β=1
α=2,β=1
α=1,β=2
'''

'''import matplotlib.pyplot as plt
import numpy as np
import os


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(alpha, beta, color):
    x = np.linspace(-2, 2, 1200)
    x = x[x != 0]
    y = (x**beta + alpha**beta) / x**beta
    plt.scatter(x, y, label = f"α={alpha}, β={beta}", color = color, s=3)

f(1, 1, 'r')
f(2, 1, 'c')
f(1, 2, 'g')

plt.axhline(y=0, color='black', linewidth = 1.5)
plt.axvline(x=0, color='black', linewidth = 1.5)

plt.ylim(-10, 10)
plt.title('График функции f(x)')
plt.legend()
plt.grid(True)
plt.show()
dir = os.getcwd()
plt.savefig(dir + '/my_first_dependence.svg')
'''

'''
2. остроить в общих осях графики для x>0.
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:

для малых x
для больших x
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций.

Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
'''
'''import matplotlib.pyplot as plt
import numpy as np
import os


fig, ax = plt.subplots(figsize=(10, 6))

ax_small_x = fig.add_axes([0.3, 0.6, 0.2, 0.2])
ax_large_x = fig.add_axes([0.6, 0.5, 0.2, 0.2])

def f(alpha, beta, color):
    x = np.linspace(0, 8, 2000)
    x = x[x != 0]
    y = (x**beta + alpha**beta) / x**beta
    ax.scatter(x, y, label = f"α={alpha}, β={beta}", color = color, s=3)
    x_large = np.linspace(6, 8, 500)
    x_small = np.linspace(0.1, 0.9, 500)
    y_large = (x_large**beta + alpha**beta) / x_large**beta
    y_small = (x_small**beta + alpha**beta) / x_small**beta
    ax_small_x.scatter(x_small, y_small, color = color, s=3)
    ax_large_x.scatter(x_large, y_large, color = color, s=3)

f(1, 1, 'r')
f(2, 1, 'c')
f(1, 2, 'g')

ax.set_title('График функции f(x)')
ax_large_x.set_title('Поведение графика при больших х')
ax_small_x.set_title('Поведение графика при малых х')
ax.set_ylim(0, 20)
ax.axhline(y=0, color='black', linewidth = 1.5)
ax.axvline(x=0, color='black', linewidth = 1.5)
ax_small_x.axhline(y=0, color='black', linewidth = 1.5)
ax_small_x.axvline(x=0, color='black', linewidth = 1.5)
ax_large_x.axhline(y=0, color='black', linewidth = 1.5)
ax_large_x.axvline(x=0, color='black', linewidth = 1.5)
ax_large_x.set_ylim(0, 2)
ax_large_x.set_xlim(6, 8)
ax_small_x.set_ylim(0, 10)
ax.legend()
plt.show()
dir = os.getcwd()
plt.savefig(dir + '/my_second_dependence.svg')
'''

'''
3. Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.

Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.

Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
'''

'''import matplotlib.pyplot as plt
import numpy as np
import os
fig, ax = plt.subplots(figsize=(10, 6))
ax_small = fig.add_axes([0.3, 0.58, 0.4, 0.25])


def f(alpha, beta, color):
    x = np.linspace(-10, 0, 2000)
    x = x[x != 0]
    y = (x**beta + alpha**beta) / x**beta
    ax.scatter(x, y, label=f"α={alpha}, β={beta}", color=color, s=3)
    x_small = np.linspace(-10000, -9996, 500)
    y_small = (x_small**beta + alpha**beta) / x_small**beta
    ax_small.scatter(x_small, y_small, color=color, s=3)


f(1, 1, 'r')
f(2, 1, 'c')
f(1, 2, 'g')

ax.set_title('График функции f(x)')
ax_small.set_title('Поведение графиков при удалении x от 0 к −∞')
ax.set_ylim(-8, 10)
ax.set_xlim(-8, 1)
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)
ax_small.axhline(y=0, color='black', linewidth=1.5)
ax_small.axvline(x=0, color='black', linewidth=1.5)
ax_small.set_ylim(0.999, 1.001)
ax_small.set_xlim(-10000, -9996)
plt.show()
dir = os.getcwd()
plt.savefig(dir + '/my_third_dependence.svg')
'''

'''
4. Построить в общих осях графики для:
α=1,β=0.5

α=1,β=−0.5

α=1,β=−1.5
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость

В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с α=1 проходят через общую точку (1, 2).

Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.

Каждый график будет содержать 4 кривые. 2 общих:

α=1,β=0 (в качестве цвета попробуйте использовать 'b--')

α=1,β=−1 (в качестве цвета попробуйте использовать 'r--')
И по 2 уникальных для каждого графика:

α=1,β=0.5 и

α=1,β=0.8

α=1,β=−0.5 и

α=1,β=−0.8

α=1,β=−1.5 и

α=1,β=−2.5

Не забудьте добавить легенду на каждый график. Для этого может потребоваться вызвать метод legend() для каждого объекта осей.
'''

import matplotlib.pyplot as plt
import numpy as np
import os
def f(x, alpha, beta):
    return (x ** beta + alpha ** beta) / x ** beta


x = np.linspace(0.01, 2, 2000)


params = [
    [(1, 0.5), (1, 0.8)],
    [(1, -0.5), (1, -0.8)],
    [(1, -1.5), (1, -2.5)]
]

plt.figure(figsize=(15, 5))
for i, param_set in enumerate(params):
    plt.subplot(1, 3, i + 1)

    plt.scatter(x, f(x, 1, 0), s=3, label='α=1,β=0', color='b')
    plt.scatter(x, f(x, 1, -1), s=3, label='α=1,β=-1', color='r')

    for alpha, beta in param_set:
        plt.scatter(x, f(x, alpha, beta), s=3, label=f'α={alpha},β={beta}')

    plt.legend()
    plt.ylim(1, 3)

plt.tight_layout()
plt.suptitle('Графики при различных α и β. Пересечение в (1, 2).')
plt.show()
dir = os.getcwd()
plt.savefig(dir + '/my_fourth_dependence.svg')
