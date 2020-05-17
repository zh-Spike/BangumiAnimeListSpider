from pyecharts import Pie
import pandas as pd
d=pd.read_csv('BGM_result.csv')
star=d["score"]
result = star.values.tolist()
attr = ["五星", "四星", "三星", "二星", "一星"]
value=[
    result.count(5.0),
    result.count(4.0),
    result.count(3.0),
    result.count(2.0),
    result.count(1.0),
]
pie_ = Pie('《明日方舟》评分星级比例', title_pos='center', width=1000)
pie_.add("score", attr, value, center=[75, 50], is_random=True,
        radius=[30, 75], rosetype='area',
        is_legend_show=False, is_labBGM_el_show=True)
pie_.render('评分.html')
