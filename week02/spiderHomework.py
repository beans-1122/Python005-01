import requests
from lxml import etree
import json

#CSDN问题页爬虫
def spider():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent':user_agent}
    #myurl = 'https://www.toutiao.com/ch/software/'
    myurl = 'https://ask.csdn.net/?spm=1000.2115.3001.4492'
    response = requests.get(myurl,headers =header)
    print('返回状态码:',response.status_code)
    html = response.text
    #print(html)
    element = etree.HTML(html)
    #print(element)
    titles = element.xpath('//div[@class="question-content-wrapper-pd question-content-wrapper"]/div[@class="title-box"]/a/h3/text()')
    for i in titles:
        print(i)


if __name__ == "__main__":
    spider()