"""
pyecharts: libraries for generating Echarts charts
Echarts: an open source JS library for data visualization from Baidu
official web: https://echarts.apache.org/
install: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
other data visualization tools: matplotlib
"""

from pyecharts.charts import Bar #bar chart
from pyecharts.charts import Pie #pie chart
from pyecharts.charts import Line #line chart
from pyecharts import options #set parameters

def main():
    count_a = {"shirt":11,"sweater":22,"skirt":33,"windbreaker":44,"T-shirt":55} #the sales volume of merchant a
    count_b = {"shirt":66,"sweater":77,"skirt":88,"windbreaker":99,"T-shirt":12} #the sales volume of merchant b
    count_c = {"shirt":34, "sweater":56, "skirt":78, "windbreaker":91, "T-shirt":23} #the sales volume of merchant c
    # print(list(count_a.keys()))
    # print(list(count_b.keys()))
    # print(list(count_c.keys()))
    # print(list(count_a.values()))
    # print(list(count_b.values()))
    # print(list(count_c.values()))

    #create a bar chart object
    bar = Bar()
    bar.add_xaxis(list(count_a.keys())) #add the x-axis data
    bar.add_yaxis("the sales volume of merchant a", list(count_a.values())) #add the y-axis data
    bar.add_yaxis("the sales volume of merchant b", list(count_b.values())) #add the y-axis data
    bar.add_yaxis("the sales volume of merchant c", list(count_c.values())) #add the y-axis data

    #set parameters
    bar.set_global_opts(
        title_opts = options.TitleOpts(
            title = "sales situation in the mall",
            pos_top = "10px",
            pos_left = "center",
            title_textstyle_opts = options.TextStyleOpts(
                font_size = 14
            )
        ),
        legend_opts = options.LegendOpts(
            pos_top = "40px",
            pos_left = "center",
        ),
        graphic_opts=[],
        tooltip_opts=options.TooltipOpts(
            trigger="axis"
        )
    )

    #generate a chart
    bar.render("sales situation in the mall.html")


    brand = ['apple','huawei','xiaomi','oppo','vivo','sansung']
    sales_volume = [12,34,56,78,91,23]
    datalist = []

    for i in range(0,len(brand)):
        a=[brand[i],sales_volume[i]]
        datalist.append(a)
    # print(datalist)

    #create a pie chart object
    pie=Pie()
    pie.add(
        "Unit: 10,000 units",
        datalist,
        center=["50%","60%"]
    )

    #set title
    pie.set_global_opts(
        title_opts=options.TitleOpts(
            title="sales situation of phone",
            pos_top="10px",
            pos_left="center",
            title_textstyle_opts=options.TextStyleOpts(
                font_size=14
            )
        ),
        legend_opts=options.LegendOpts(
            pos_top="40px",
            pos_left="center",
            orient="horizontal"
        ),
        graphic_opts=[],
        tooltip_opts=options.TooltipOpts(
            trigger="item"
        )
    )

    # generate a chart
    pie.render("sales situation of phone.html")


    month=['january','february','march','april','may','june','july','august','september','october','november','december']
    beijin_rainfall=[12,34,56,78,91,23,45,67,89,12,34,56]
    shanghai_rainfall=[98,76,54,32,19,87,65,43,21,98,76,54]

    line=Line()
    line.add_xaxis(month)
    line.add_yaxis('beijin',beijin_rainfall)
    line.add_yaxis('shanghai',shanghai_rainfall)

    line.set_global_opts(title_opts=options.TitleOpts(title='city rainfall'))

    line.render("city rainfall.html")

if __name__ == '__main__':
    main()