from pyecharts import Bar, Pie, Line
import pandas as pd
import re
d = pd.read_csv('Movie_Time.csv', nrows=250)
f = pd.read_csv('TV_Time.csv', nrows=250)
year_0 = d["year"]
month_0 = d["month"]
result_movie_year = year_0.values.tolist()
result_movie_month = month_0.values.tolist()
result_mv_year = pd.value_counts(result_movie_year)
result_mv_month = pd.value_counts(result_movie_month)

year_1 = f["year"]
month_1 = f["month"]
result_TV_year = year_1.values.tolist()
result_TV_month = month_1.values.tolist()
result_tv_year = pd.value_counts(result_TV_year)
result_tv_month = pd.value_counts(result_TV_month)


month1 = result_tv_month[1.0] + result_mv_month[1.0]
month2 = result_tv_month[2.0] + result_mv_month[2.0]
month3 = result_tv_month[3.0] + result_mv_month[3.0]
month4 = result_tv_month[4.0] + result_mv_month[4.0]
month5 = result_tv_month[5.0] + result_mv_month[5.0]
month6 = result_tv_month[6.0] + result_mv_month[6.0]
month7 = result_tv_month[7.0] + result_mv_month[7.0]
month8 = result_tv_month[8.0] + result_mv_month[8.0]
month9 = result_tv_month[9.0] + result_mv_month[9.0]
month10 = result_tv_month[10.0] + result_mv_month[10.0]
month11 = result_tv_month[11.0] + result_mv_month[11.0]
month12 = result_mv_month[12.0]
#tv_month值为0，找不到其标签值


result_year = result_tv_year.add(result_mv_year, fill_value=0)
sum_80 = 0
sum_90 = 0
sum_00 = 0
sum_10 = 0
sum_40 = int(result_year[1940])
sum_70 = int(result_year[1979])
for index1 in range(1982, 1987):
    sum_80 += int(result_year[index1])
sum_80 = sum_80 + int(result_year[1988]) + int(result_year[1989])
for index2 in range(1992, 2000):
    sum_90 += int(result_year[index2])
for index3 in range(2001, 2010):
    sum_00 += int(result_year[index3])
for index4 in range(2010, 2020):
    sum_10 += int(result_year[index4])
sum_20 = int(result_year[2020])

year_tv_40 = result_tv_year[1940]
year_tv_70 = result_tv_year[1979]
year_tv_80 = result_tv_year[1983] + result_tv_year[1985] + \
    result_tv_year[1986] + result_tv_year[1989]
year_tv_90 = result_tv_year[1993] + result_tv_year[1995] + result_tv_year[1996] + \
    result_tv_year[1997] + result_tv_year[1998] + result_tv_year[1999]
year_tv_00 = result_tv_year[2001] + result_tv_year[2002] + result_tv_year[2003]+result_tv_year[2004] + \
    result_tv_year[2005] + result_tv_year[2006] + \
    result_tv_year[2007] + result_tv_year[2008] + result_tv_year[2009]
year_tv_10 = result_tv_year[2010] + result_tv_year[2011] + result_tv_year[2012] + result_tv_year[2013]+result_tv_year[2014] + \
    result_tv_year[2015] + result_tv_year[2016] + \
    result_tv_year[2017] + result_tv_year[2018] + result_tv_year[2019]
year_tv_20 = result_tv_year[2020]

year_mv_40 = 0
year_mv_70 = 0
year_mv_80 = result_mv_year[1982] + result_mv_year[1984] + \
    result_mv_year[1986] + result_mv_year[1988]
year_mv_90 = result_mv_year[1992] + result_mv_year[1993] + result_mv_year[1994] + \
    result_mv_year[1995] + result_mv_year[1997] + \
    result_mv_year[1998] + result_mv_year[1999]
year_mv_00 = result_mv_year[2001] + result_mv_year[2003] + result_mv_year[2004] + result_mv_year[2005] + \
    result_mv_year[2006] + result_mv_year[2007] + \
    result_mv_year[2008] + result_mv_year[2009]
year_mv_10 = result_mv_year[2010] + result_mv_year[2011] + result_mv_year[2012] + result_mv_year[2013] + \
    result_mv_year[2015] + result_mv_year[2016] + \
    result_mv_year[2017] + result_mv_year[2018] + result_mv_year[2019]
year_mv_20 = 0

value_month = [
    month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12
]
data_month_tv = [
    result_tv_month[1.0], result_tv_month[2.0], result_tv_month[3.0], result_tv_month[4.0], result_tv_month[5.0], result_tv_month[
        6.0], result_tv_month[7.0], result_tv_month[8.0], result_tv_month[9.0], result_tv_month[10.0], result_tv_month[11.0], 0
]
data_month_mv = [
    result_mv_month[1.0], result_mv_month[2.0], result_mv_month[3.0], result_mv_month[4.0], result_mv_month[5.0], result_mv_month[
        6.0], result_mv_month[7.0], result_mv_month[8.0], result_mv_month[9.0], result_mv_month[10.0], result_mv_month[11.0], result_mv_month[12.0]
]


value_year = [
    sum_40, sum_70, sum_80, sum_90, sum_00, sum_10, sum_20
]
data_year_tv = [
    year_tv_40, year_tv_70, year_tv_80, year_tv_90, year_tv_00, year_tv_10, year_tv_20
]
data_year_mv = [
    year_mv_40, year_mv_70, year_mv_80, year_mv_90, year_mv_00, year_mv_10, year_mv_20
]


attr_month = ["1月", "2月", "3月", "4月", "5月",
              "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
attr_year = ["40年代", "70年代", "80年代", "90年代", "新世纪", "10年代", "20年代"]


pie_ = Pie('Top250动画上映月份', title_pos='center', width=1000)
pie_.add("number", attr_month, value_month, center=[75, 50], is_random=True,
         radius=[30, 75], rosetype='area',
         is_legend_show=False, is_label_show=True)
pie_.render('Top250动画上映月份.html')

bar_month = Bar('剧场版和TV上映月份对比图')
bar_month.add('剧场版动画', attr_month, data_month_mv, is_stack=True)
bar_month.add('TV动画', attr_month, data_month_tv, is_stack=True)
bar_month.render('Top250剧场版动画和TV动画上映月份对比图.html')


pie_year = Pie('Top250动画上映年代', title_pos='center', width=1000)
pie_year.add("number", attr_year, value_year, center=[75, 50], is_random=True,
             radius=[30, 75], rosetype='area',
             is_legend_show=False, is_label_show=True)
pie_year.render('Top250动画上映年代.html')

line_year = Line('剧场版和TV上映年份对比图')
line_year.add('剧场版动画', attr_year, data_year_mv, is_stack=True)
line_year.add('TV动画', attr_year, data_year_tv, is_stack=True)
line_year.render('Top250剧场版动画和TV动画上映年份对比图.html')
