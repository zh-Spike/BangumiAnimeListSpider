import csv
import pandas as pd
d = pd.read_csv(r'D:\Spider\AnimeSpider\BGM.csv', usecols=['Tip'])
huashu = []
shijian = []
jiandu = []
for i in range(1000):
    x = []
    y = []
    z = []
    str = d.values[i][0].split('/')
    flag = 0
    if len(str):
        for j in str:
            if flag == 0:
                x.append(j)
            elif flag == 1:
                y.append(j)
            else:
                z.append(j)
            flag += 1
    else:
        x.append('')
        y.append('')
        z.append('')
    huashu.append(x)
    shijian.append(y)
    jiandu.append(z)

print(huashu)
print(len(huashu))
print(shijian)
print(len(shijian))
print(jiandu)
print(len(jiandu))

name = ['huashu']
name_1 = ['shijian']
name_2 = ['jiandu1', 'jiandu2', 'jiandu3', 'jiandu4']
test = pd.DataFrame(columns=name, data=huashu)
test_1 = pd.DataFrame(columns=name_1, data=shijian)
test_2 = pd.DataFrame(columns=name_2, data=jiandu)
test.to_csv(r'D:\Spider\AnimeSpider\BGM_huashu.csv', encoding='UTF-8')
test_1.to_csv(r'D:\Spider\AnimeSpider\BGM_shijian.csv', encoding='UTF-8')
test_2.to_csv(r'D:\Spider\AnimeSpider\BGM_jiandu.csv', encoding='UTF-8')
