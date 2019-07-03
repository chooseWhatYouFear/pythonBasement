from selenium import webdriver
import time

chrome = webdriver.Chrome()

def getNovel(url):
    chrome.get(url)

    while True:
        # 标题和内容
        title = chrome.find_element_by_tag_name("h1").text

        content = chrome.find_element_by_id("content").text

        next_chapter = chrome.find_elements_by_xpath("//div[@class='jump']/a")

        # 写入文件
        with open(r"武炼巅峰.txt",'a',encoding="utf-8") as f:
            f.write(" "*30+title+"\n")
            f.write(content+'\n\n')
        if title=="章节目录 第四千七百九十五章 打秋风":
            break
        next_chapter[4].click()
    chrome.close()
getNovel("https://www.jjshu.net/0/635/8908278.html")