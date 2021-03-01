# Bangumi_AnimeList_Spider
use scrapy to get the basic information.
## v1
* 使用的是Item，最原始。
* 实现了巧妙地翻页
## v2
* 重构了部分代码，优化了部分细节。
* 发现会固定缺失部分数据，总结发现是并发数的问题，16线程并发，而网页一有24个元素，所以到page5以后会应为delay值小的原因，稳定缺失8个元素，通过修改setting.py改为24线程后解决该问题。
## v3
* 又重构了代码，使用了Itemloader，增加了可读性。
* 在item.py里实现正则化提取
* 使用pyechart和worldcloud实现数据可视化。
  
## Todo
* 数据清洗对value_counts()还存在一定问题
* 从v2开始放弃了多级页面的Itemloader对评论爬取，存在数据串行,原理和summary部分应该没差?
