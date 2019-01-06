from pyquery import PyQuery as pq
import requests

Movies = []
Score = []
Update_time = []
Board_content = []


def pare_page(url):
    # 对于有些禁止爬虫的网站，设置headers来模拟浏览器登陆
    headers = {
        'Host': "maoyan.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode("utf8")
    doc = pq(text)

    # 获取电影名
    movie_item_info = doc('div').filter('.movie-item-info')
    movie_names = movie_item_info('p').filter(".name")
    # movie_names=names('a').attr('title')

    for movie_name in movie_names.items('a'):
        # print(type(movie_name.text()))
        Movies.append(movie_name.text())

    # 猫眼网站电影的评分是两个标签，所以要分别取出来再合并
    score_integers = doc('i').filter('.integer')
    score_fractions = doc('i').filter('.fraction')
    integers = []
    fractions = []
    for score_integer in score_integers.items('i'):
        integers.append(score_integer.text())
    for score_fraction in score_fractions.items('i'):
        fractions.append(score_fraction.text())
    for i in range(len(integers)):
        Score.append(integers[i] + fractions[i])
    # 获取更新时间
    Update_time.append(doc('p').filter('.update-time').text())
    # 获取榜单规则
    Board_content.append(doc('p').filter('.board-content').text())

def main():
    num = 0
    for i in range(0, 10):
        if i == 0:
            url = "http://maoyan.com/board/4"
        else:
            url = "http://maoyan.com/board/4" + "?offset=" + str(i * 10)
        pare_page(url)
    # 输出
    print(Update_time[0])
    print(Board_content[0])
    for i in range(len(Movies)):
        print("Top" + str(num + 1) + "：" + Movies[i] + "    评分：" + Score[i])
        num=num+1

if __name__ == '__main__':
    main()
