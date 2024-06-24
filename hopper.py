import numpy as np
import math
import matplotlib.pyplot as plt
from Coord import Coordinates


# функция для расчета координат для каждой оси
def funnel(coordinates, rule):
    coord, new_coords = 0, []
    for dx in coordinates:
        new_coords.append(coord + dx)
        coord = rule(coord, dx)
    return new_coords


def mean(xs): return sum(xs) / len(xs)


def stddev(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))


def experiment(label, rule):
    coordinates = Coordinates(0, 1, 50)
    rxs, rys = funnel(coordinates.x, rule), funnel(coordinates.y, rule)
    print(label)
    print(f'Mean x, y    : %.4f, %.4f' % (mean(rxs), mean(rys)))
    print('Std dev x, y : %.4f, %.4f' % (stddev(rxs), stddev(rys)))
    print()
    return [rxs, rys]


rule1_coords = experiment('Rule 1:', lambda z, dz: 0)  # никак не пересчитываем координаты
rule2_coords = experiment('Rule 2:', lambda z, dz: -dz)  # делаем координаты с противоположным знаком (перемещение относительно текущей позиции)
rule3_coords = experiment('Rule 3:', lambda z, dz: -(z + dz))  # Опять противоположные координаты, но относительно центра
rule4_coords = experiment('Rule 4:', lambda z, dz: z + dz)  # перемещаем воронку над последней позицией шарика

# условно говоря правило 3 - зеркальное отражение позиции
# а правило 2 - это движение в противоположную сторону

# Перемещение осей координат в центр
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.subplot(2, 2, 1)
plt.scatter(rule1_coords[0], rule1_coords[1])
plt.xlim(-7, 7)
plt.ylim(-7, 7)
# Добавление надписей и заголовка
plt.title('1st rule')

# Отображение графика
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(rule2_coords[0], rule2_coords[1])
plt.xlim(-7, 7)
plt.ylim(-7, 7)
# Добавление надписей и заголовка
plt.title('2nd rule')

plt.subplot(2, 2, 3)
plt.scatter(rule3_coords[0], rule3_coords[1])
plt.xlim(-7, 7)
plt.ylim(-7, 7)
# Добавление надписей и заголовка
plt.title('3rd rule')

plt.subplot(2, 2, 4)
plt.scatter(rule4_coords[0], rule4_coords[1])
plt.xlim(-7, 7)
plt.ylim(-7, 7)
# Добавление надписей и заголовка
plt.title('4th rule')
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# Отображение графика
plt.show()
