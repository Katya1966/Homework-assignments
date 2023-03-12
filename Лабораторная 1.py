#MATH
#1. Найти корни квадратного уравнения ax^2 + bx + c (math.sqrt)
import math
a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4*a*c

if D < 0:
    print('no square roots found')
elif D == 0:
    x = -b / 2*a
    print(x)
else:
    x1 = -b + math.sqrt(D) / 2*a
    x2 = -b + math.sqrt(D) / 2*a
    print(x1)
    print(x2)


#2. Найти площадь круга (from math import pi)
import math
R = float(input())
area = math.pi*R*R
print(area)

#COUNTER
#1. Вывести элементы массива, которые встречаются только один раз (или два/три/четыре раза), причём в том порядке, в котором они идут в массиве.
from collections import Counter
array = [78, 59, 34, 23, 67, 66, 66, 23, 65, 59, 100, 100, 100, 200, 205]
count = []
for key, value in Counter(array).items():
    if value == 3:
        count.append(key)
print(count)


#2. Дан массив a из n целых чисел. Напишите программу, которая найдет наибольшее число, которое чаще других встречается в массиве (т.е. если три числа встречаются одинаковое количество раз, нужно найти наибольшее из них).
from collections import Counter
import random
a = []

n = int(input("n= "))
for i in range(n):
    x = random.randint(1,100)
    a.append(x)

def most_common_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common()
    max_count = most_common[0][1]
    result = most_common[0][0]
    for elem, count in most_common:
        if count == max_count and elem > result:
            result = elem
    return result
print(a)
print(most_common_element(a))


#ITERTOOLS
#Задача 1.
import itertools
k = 0
a = list(itertools.product('атом', repeat=6))
for x in a:
    if x.count('м') == 1:
        k += 1
print(k)

#Задача 2.
import itertools
k = 0
a = list(itertools.permutations('НЕБО'))
print(len(set(a)))

#CYCLE
from itertools import cycle

def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result
print(infinite([2, 5, 8], 7))
print(infinite([], 1000))
print(infinite([7], 4))


#ОБРАБОТКА ДАННЫХ JSON
# С помощью json модуля напишите скрипт, который считывает файл JSON, содержащий информацию о книгах (название, авторов, ISBN, количество страниц, статус публикации, тематику и т.д.), и выводит список всех книг, в которых количество страниц больше 500.

import json
from pprint import pprint

with open('books.json') as q:
    data = json.load(q)

for i in data:
    if i['pageCount'] > 500:
        pprint(i['title'])



#МАНИПУЛИРОВАНИЕ ДАННЫМИ CSV
# 1. Файл freshman_kgs.csv

import pandas as pd

data = pd.read_csv("freshman_kgs.csv")
data.columns = data.columns.str.replace('"','')
data = data.assign(Difference = data[" Weight (Sep)"] - data[" Weight (Apr)"])
result = data.loc[(data["Sex"] == "M") & (data["Difference"] >= 0) & (data[" BMI (Apr)"] > 20)]
print(result)

result.to_csv("new_freshman_kgs.csv")

#2.Файл homes.csv

import pandas as pd
import numpy as np

data = pd.read_csv("homes.csv")
data.columns = data.columns.str.replace('"','')
data[" House"] = np.where((data["Sell"]>180) & (data[" Taxes"]<3500), "house", "no")
sell = data[(data[" Rooms"] == 8)]["Sell"]
mean = sell.describe()['mean']
print("Среднее значение:", mean)
print(' ')
print(data)

data.to_csv("new_homes.csv")




















