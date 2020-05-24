import csv
import pandas as pd
d = pd.read_csv(r'Ex_Final.csv', usecols=['director'])
jiandu = []
for i in range(5800):
    x = []
    str = d.values[i]
    if len(str):
        for j in str:
            x.append(j)
    else:
        x.append('')
    jiandu.append(x)

print(jiandu)


name = ['jiandu']
test = pd.DataFrame(columns=name, data=jiandu)
test.to_csv(r'D:\Spider\AnimeSpider\BGM_jiandu_v2.csv', encoding='UTF-8')
