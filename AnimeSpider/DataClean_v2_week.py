import csv
import pandas as pd
d = pd.read_csv(r'Ex_Finalv2.csv', usecols=['week'])
week = []
for i in range(5800):
    x = []
    str = d.values[i]
    if len(str):
        for j in str:
            x.append(j)
    else:
        x.append('')
    week.append(x)

print(week)


name = ['week']
test = pd.DataFrame(columns=name, data=week)
test.to_csv(r'D:\Spider\AnimeSpider\BGM_week_v1.csv', encoding='UTF-8')
