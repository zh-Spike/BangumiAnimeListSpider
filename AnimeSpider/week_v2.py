from pyecharts import Bar
import pandas as pd
import re
d = pd.read_csv('BGM_week_v1.csv', nrows=250)
star = d["week"]
result = star.values.tolist()
result1 = pd.value_counts(result)
sum_ = 0
week1 = result1["星期一"]
week2 = result1["星期二"] + result1["火曜日"]
week3 = result1["星期三"] + result1["水曜日"]
week4 = result1["星期四"] + result1["周四"] + result1["木曜日"]
week5 = result1["星期五"]
week6 = result1["星期六"]
week7 = result1["星期天"] + result1["周日"]

value = [
    week1, week2, week3, week4, week5, week6, week7
]

for i in value:
    sum_ += i
other = 250-sum_
value.append(other)
attr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日", "剧场版"]
bar = Bar('Top250动画 TV动画放送日期', "count")
bar.add("count", attr, value)
bar.render('Top250动画 TV动画放送日期.html')
