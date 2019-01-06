# encoding:utf-8
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    respones = requests.get(url)
    # print(respones.text)是乱码，需要解码
    # print(respones.content.decode("utf8"))
    text = respones.content.decode("utf8")
    # soup=BeautifulSoup(text,"lxml")
    soup = BeautifulSoup(text, "html5lib")  # 解析网页功能更强，但是速度慢
    conMidtab = soup.find('div', class_='conMidtab')
    # print(conMidtab)
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            # print(type(tds[0]))
            city_name = list(tds[0].stripped_strings)[0]
            if (index == 0):
                city_name = list(tds[1].stripped_strings)[0]
            # print(city_name)
            min_temp = list(tds[-2].stripped_strings)[0]
            # print(min_temp)
            ALL_DATA.append({"city": city_name, "min_temp": int(min_temp)})
            # print({"city:":city_name,"min_temp":int(min_temp)})


def main():
    area_url = {"hb": "http://www.weather.com.cn/textFC/hb.shtml",
                "db": "http://www.weather.com.cn/textFC/db.shtml",
                "hd": "http://www.weather.com.cn/textFC/hd.shtml",
                "hz": "http://www.weather.com.cn/textFC/hz.shtml",
                "hn": "http://www.weather.com.cn/textFC/hn.shtml",
                "xb": "http://www.weather.com.cn/textFC/xb.shtml",
                "xn": "http://www.weather.com.cn/textFC/xn.shtml",
                "gat": "http://www.weather.com.cn/textFC/gat.shtml"}
    for key in area_url.keys():
        # url="http://www.weather.com.cn/textFC/hb.shtml"
        url = area_url[key]
        parse_page(url)
    # 分析数据
    # 对最低气温进行排序
    ALL_DATA.sort(key=lambda data: data["min_temp"])
    data = ALL_DATA[0:10]
    # print(data)
    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda y: y['min_temp'], data))
    chart = Bar("中国天气最低气温排行榜")
    chart.add("气温℃", cities, temps)
    chart.render("temperature.html")
    print("视图生成完毕！")


if __name__ == '__main__':
    main()
