import requests
from bs4 import BeautifulSoup
def getUrlContent(url, params={}):
    content = requests.get(url, params).content
    return content

def getNovelUrlByTitle(content, keyword=''):
    soup = BeautifulSoup(content, "html.parser")
    ele = soup.find('a', title=keyword)
    if(ele['href']):
        print('获取小说地址成功')
    else:
        print('获取小说地址失败')
    return ele['href']

def getNovelUrlListById(content, keyword=''):
    soup = BeautifulSoup(content, "html.parser")
    ele = soup.find('div', id=keyword)
    aList = ele.find_all('a')
    urlList = []
    for a in aList:
        urlList.append(a['href'])
    
    if(len(urlList) > 0):
        print('获取小说章节地址成功')
        print('一共' + str(len(urlList) + 1) + '章')
    else:
        print('获取小说章节地址失败')

    return urlList

def getNovelContent(content, keyword=''):
    soup = BeautifulSoup(content, "html.parser")
    cont = soup.find('div', id='content').get_text()
    title = soup.find('div', class_='bookname').find('h1').get_text()
    return cont, title

