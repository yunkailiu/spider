# 图片爬虫：爬取淘宝的图片

import urllib.request
import re

keyname = "连衣裙"
key = urllib.request.quote(keyname)

for i in range(0, 2):
    url = "https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.4.5af911d9RnfrEY&q=" + key + "&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=" + str(i * 60)
    print(url)
    print("")
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")

    pat = '"pic_url":"//(.*?)jpg"'
    imagelist = re.compile(pat).findall(data)  # 图片的网站
    # print(imagelist)
    # print("")
    m=0
    # 下面循环爬取每一页中所有的图片
    for j in range(0, len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = "http://" + thisimg + "jpg"
        file = "imags/" + str(i) + "-" + str(j) + ".jpg"
        print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
        urllib.request.urlretrieve(thisimgurl, filename=file)
        m=m+1
print("Download complete!")




