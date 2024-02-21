'''
Задание 1
Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

    {"less than high school":0.2,
    "high school":0.4,
    "more than high school but not college":0.2,
    "college":0.2}
def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    raise NotImplementedError()
'''

import pandas as pd
import scipy.stats as stats

file = input("Укажите путь к нужному файлу: ")
data = pd.read_csv(file + r'\NISPUF17.csv')

def proportion_of_education(data):
    total_count = data['EDUC1'].count()  # Считаем общее количество записей
    # Считаем количество вхождений для каждого уровня образования
    education_counts = data['EDUC1'].value_counts().sort_index()
    proportion = education_counts / total_count  # Считаем пропрорцию
    dictionary = {"less than high school": proportion[1],
                  "high school": proportion[2],
                  "more than high school but not college": proportion[3],
                  "college": proportion[4]}
    return dictionary


print(proportion_of_education(data))
print("--------------------------------------------")



'''
Задание 2
Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

This function should return a tuple in the form (use the correct numbers:

(2.5, 0.1)
def average_influenza_doses():
    # YOUR CODE HERE
    raise NotImplementedError()

assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."
'''
import pandas as pd
import scipy.stats as stats

file = input("Укажите путь к нужному файлу: ")
data = pd.read_csv(file + r'\NISPUF17.csv')


def average_influenza_doses(data):
    # Фильтрация данных для детей, которых кормили и не кормили грудью
    received_breast_milk = data[data['CBF_01'] == 1]['P_NUMFLU']
    not_received_breast_milk = data[data['CBF_01'] == 2]['P_NUMFLU']
    # Расчет среднего количества вакцин
    avg_breastfed = received_breast_milk.mean()
    avg_not_breastfed = not_received_breast_milk.mean()

    return (avg_breastfed, avg_not_breastfed)


assert len(average_influenza_doses(data)) == 2

# Вызов функции и сохранение результата в переменную
print(average_influenza_doses(data))

feed, not_feed = average_influenza_doses(data)

print(f'Среднее количество вакцин для детей, которых кормили грудью равно: {feed}')
print(f'Среднее количество вакцин для детей, которых не кормили грудью равно: {not_feed}')
print("--------------------------------------------")


'''
Задание 3
It would be interesting to see if there is any evidence of a link between vaccine 
effectiveness and sex of the child. Calculate the ratio of the number of children 
who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus 
those who were vaccinated but did not contract chicken pox. Return results by sex.

This function should return a dictionary in the form of (use the correct numbers):
    {"male":0.2,
    "female":0.4}
    
Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder 
is looking for starts with the digits 0.0077.
'''

def chickenpox_by_sex(data):
    # Фильтрация данных для исключения записей с отказом от ответа или пропущенными данными
    valid_data = data[(data['HAD_CPOX'] == 1) | (data['HAD_CPOX'] == 2)]
    valid_data = valid_data.dropna(subset=['P_NUMVRC'])

    # Разделение данных по полу
    males = valid_data[valid_data['SEX'] == 1]
    females = valid_data[valid_data['SEX'] == 2]

    # Функция для расчета соотношения
    def computation_ratio(group):
        vaccinated = group[group['P_NUMVRC'] > 0]  # Вакцинированные (по крайней мере одна доза)
        rescheduled = vaccinated[vaccinated['HAD_CPOX'] == 1]  # Перенесли ветрянку после вакцинации
        not_rescheduled = vaccinated[vaccinated['HAD_CPOX'] == 2]  # Не перенесли ветрянку после вакцинации
        return rescheduled.shape[0] / not_rescheduled.shape[0] if not_rescheduled.shape[0] > 0 else 0

    # Расчет соотношения для каждого пола
    male_ratio = computation_ratio(males)
    female_ratio = computation_ratio(females)

    return {'male': male_ratio, 'female': female_ratio}


# Вызываем функцию и выводим результат
chickenpox_by_sex_result = chickenpox_by_sex(data)
print(chickenpox_by_sex_result)
print("--------------------------------------------")
