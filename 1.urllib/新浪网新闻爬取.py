import urllib.request
import re
data=urllib.request.urlopen("http://news.sina.com.cn/").read().decode("utf8")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data)
m=0
for i in range(0,len(allurl)):
    thisurl=allurl[i]
    file="sinanews/"+str(i)+".html"
    print('***** ' + str(m) + '.html *****' + '   Downloading...')
    urllib.request.urlretrieve(thisurl,file)
    m=m+1
print("Download complete!")