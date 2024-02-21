'''
1. Создать объект pandas Series из листа, объекта NumPy, и словаря
'''

'''import pandas as pd
import numpy as np


my_series = pd.Series([5, 6, 7, 8, 9, 10])
my_array = pd.Series(np.array([5, 6, 7, 8, 9, 10]))
my_dictionary = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 9, 'e': 3, 'f': 4})
print(f"Объект Pandas из листа: \n{my_series}")
print(f"Объект Pandas из Numpy: \n{my_array}")
print(f"Объект Pandas из словаря: \n{my_dictionary}")
'''

'''
2. Получить не пересекающиеся элементы в двух объектах Series
'''
'''import pandas as pd
import numpy as np

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

# Используем функцию .isin() для нахождения общих элементов, а затем отфильтровываем их
unique_in_series1 = series1[~series1.isin(series2)]
unique_in_series2 = series2[~series2.isin(series1)]

# Объединяем уникальные элементы из обоих Series
unique_elements = pd.concat([unique_in_series1, unique_in_series2]).reset_index(drop=True)
print(unique_elements)
'''

'''
3. Узнать частоту уникальных элементов объекта Series (гистограмма)
'''
'''import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


series = pd.Series(np.random.randint(0, 10, 100))
unique = series.value_counts().sort_index()

plt.figure(figsize=(10, 6))
unique.plot(kind='bar')
plt.title('Частота уникальных элементов в Series')
plt.xlabel('Уникальные элементы')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
'''


'''
4. Объединить два объекта Series вертикально и горизонтально
'''
'''import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
series2 = pd.Series([9, 10, 11, 12, 13, 14, 15, 16])
vertical_concat = pd.concat([series1, series2], axis=0)  #Вертикальный столбец 
horizontal_concat = pd.concat([series1, series2], axis=1)  #горизонтальная строка
print(f"Объединение по вертикали: \n{vertical_concat}")
print(f"Объединение по горизонтали: \n{horizontal_concat}")
'''

'''
5. Найти разность между объектом Series и смещением объекта Series на n
'''

import pandas as pd


data = {'A': [1, 2, 3, 4, 5]}
series = pd.Series(data['A'])

# Задаем количество шагов для смещения
n = 2

# Вычисляем разность между объектом Series и его смещением на n шагов
difference = series - series.shift(n)

print(difference)
