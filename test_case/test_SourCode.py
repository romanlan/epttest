#coding: utf-8
import urllib
import re
import UrlList

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
# def findChar(h):


if __name__ == "__main__":
    url = UrlList.en_url
    for num in range(0, 15):
        html = getHtml(url[num])
        location_img = re.findall('"//img\S*"', html)
        location_js = re.findall('"\S*.js"', html)
        location_css = re.findall('"\S*.css"', html)
        doc_html = '..\\text\\'+str(num)+'_en.txt'
        my_file = open(doc_html, 'w')
        # 清除文本内容
        my_file.truncate()
        my_file.write(url[num] + '\n')
        for i in location_img:
            my_file.write(i + '\n')
        for i in location_js:
            my_file.write(i + '\n')
        for i in location_css:
            my_file.write(i + '\n')





