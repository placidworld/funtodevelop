# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:59:26 2020

@author: heart
"""


import random
import datetime 
import pyecharts.options as opts

 #Calendar
from pyecharts.charts import Calendar
begin = datetime.date(2019,1,1)
end = datetime.date(2019,12,31)

data = [[str(begin+datetime.timedelta(days = i)),random.randint(1000,25000)] for i in range((end-begin).days + 1)]
print(data)
c = (
	Calendar(init_opts = opts.InitOpts(width = "1000px",height = "500px"))
		.add(
			series_name ="",
			yaxis_data = data,
			calendar_opts = opts.CalendarOpts(
				pos_top = "120",
				pos_left = "30",
				pos_right = "30",
				range_ = "2019",
				yearlabel_opts = opts.CalendarYearLabelOpts(is_show = False),

				),
			)
		.set_global_opts(
			title_opts = opts.TitleOpts(pos_top = "30",pos_left = "center",title = "2019 Steps Walked"),
			visualmap_opts=opts.VisualMapOpts(
            	max_=20000, min_=500, orient="horizontal", is_piecewise=False
        	),

		)
		.render("calendar_heatmap.html")

	)


# Funnel 
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

c = (
	Funnel()
	.add(
		"Merchants",
		[list(z) for z in zip(Faker.choose(), Faker.values())],
		sort_ = "ascending",
		label_opts = opts.LabelOpts(position = "inside"),

		)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Funnel-Sort(ascending)"))
	.render("funnel_sort_ascending.html")

	)


# Dashboard
from pyecharts.charts import Gauge
g = (
	Gauge()
	.add(
		"",
		[("Completion Rate",66.6)],
		detail_label_opts = opts.GaugeDetailOpts(
			offset_center = [0,"40%"],
			font_size = 30,

			),

		)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Gauge-Basics"))
	.render("gauge_base.html")

	)

# 关系图
from pyecharts.charts import Graph
nodes = [
	{"name": "Point 1", "symbolSize": 10},
    {"name": "Point 2", "symbolSize": 20},
    {"name": "Point 3", "symbolSize": 30},
    {"name": "Point 4", "symbolSize": 40},
    {"name": "Point 5", "symbolSize": 50},
    {"name": "Point 6", "symbolSize": 40},
    {"name": "Point 7", "symbolSize": 30},
    {"name": "Point 8", "symbolSize": 20},
	
]

links = []
for i in nodes:
	for j in nodes:
		links.append({"source":i.get("name"),"target":j.get("name")})
g = (
	Graph()
	.add("",nodes,links,repulsion = 8000)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Graph-基本示例"))
	.render("graph_base.html")
	)


import json
# 关系图——微博
# json文件的数据结构
# [
# [{},{},...,{}],
# [{},{},...,{}],
# [{},{},...,{}]
# ]
# 第一个是node，第二个是link,第三个是category
# node的数据结构
# 			{
#             "name": "Camel3942",
#             "symbolSize": 5,
#             "draggable": "False",
#             "value": 1,
#             "category": "Camel3942",
#             "label": {
#                 "normal": {
#                     "show": "True"
#                 }
#             }
#         }

# 如果“Camel3942”的微博被"A"转发了，则"Camel3942"的category还是"Camel3942","A"的category是"Camel3942"

# link
# {
# "source":"Camel3942",
# "target":"A",
# 
# }
# source表示元微博博主，target表示转发微博的微博博主
# category
# {
# "name":"Camel3942"
# 
# }
# 如果“Camel3942”的微博被“A”转发了
with open("weibo.json","r",encoding = "utf-8") as f:
	j = json.load(f)
	nodes,links,categories,cont,mid,userl = j
c = (
	Graph()
	.add(
		"",
		nodes,
		links,
		categories,
		repulsion = 50,
		linestyle_opts = opts.LineStyleOpts(curve = 0.2),
		label_opts = opts.LabelOpts(is_show = False),
		)
	.set_global_opts(
		legend_opts = opts.LegendOpts(is_show = False),
		title_opts = opts.TitleOpts(title = "Graph - Weibo Forward Relationship Map"),
		)
	.render("graph_weibo.html")

	)

