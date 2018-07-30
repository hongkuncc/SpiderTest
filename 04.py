# -*- coding: utf-8 -*-
from selenium import webdriver
import time

url = 'https://weibo.com/1223178222/GrBAgD95Q?from=page_1004061223178222_profile&amp&wvr=6&amp&mod=weibotime'

def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def find_info():
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text)for el in elems[1:]]

while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6)
    info = find_info()
    rep,comm,like = info()
    if rep >30000:
        print('你关注的微博转发量已经过'+str(rep))
        print('你喜欢的微博转发量以超过{rep}')
        break
    else:
        print('Not happening')

    time.sleep(1200)

print('Done!')