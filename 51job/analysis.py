import re
import numpy as np
import matplotlib.pyplot as plt

with open('job.txt', 'r') as jb:
    data = str(jb.readlines())

name = re.findall('职位名:.*?\s', data)
company = re.findall('工作地点:.*?\s', data)
moneys = re.findall('工资:.*?\s', data)
place = set()
money = []
RMB = []
for i, j, k in zip(name, company, moneys):
    if 'Java' not in i and 'JAVA' not in i and 'C' not in i and 'php' not in i and 'PHP' and 'c' not in i and float(re.sub('工资:|\s', '', k)) != 0.0:
        place.add(re.sub('工作地点:|\s', '', j))
place = list(place)
for i in range(len(place)):
    money.append([])
for j, k in zip(company, moneys):
    if re.sub('工作地点:|\s', '', j) in place and float(re.sub('工资:|\s', '', k)) != 0.0:
        money[place.index(re.sub('工作地点:|\s', '', j))].append(float(re.sub('工资:|\s', '', k)))

for i in range(len(place)):
    RMB.append(round(sum(money[i])/len(money[i]), 2))

a, b = [], []
for ii in range(21):
    a.append(max(RMB))
    b.append(place[RMB.index(max(RMB))])
    place.remove(place[RMB.index(max(RMB))])
    RMB.remove(max(RMB))

plt.title(u'Python各地区工资分布图')
colors = ['b', 'g', 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'c', 'turquoise', 'm', 'gray', 'r',
          'lightgray', 'lime', 'skyblue', 'purple', 'peru',  'dimgray', 'orange', 'olive', 'g']

x = np.arange(len(a))
plt.bar(range(len(a)), a, width=0.9, tick_label=b, color=colors)
for _a, _b in zip(x, a):
    plt.text(_a, _b+0.9, '%d元/月' % _b, ha='center', va='bottom', fontsize=10)
plt.show()