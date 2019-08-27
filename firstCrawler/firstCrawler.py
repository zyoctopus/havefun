# -*- coding: utf-8 -*

import requests
import pprint
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://movie.douban.com/top250'

# 获取目标页面的content内容
def download_page_content(url, params={}):
    content = requests.get(url, params).content
    return content

# 获取html中的目标内容
def parse_html(html):
    _html = BeautifulSoup(html, "html.parser")
    lis = _html.find('ol', 'grid_view').find_all('li')

    movie_title_list = []

    if lis:
        for li in lis:
            text = li.find('div', attrs={'class': 'info'}).find(
                'div', attrs={'class': 'hd'}).find('span', attrs={'class': 'title'}).get_text()
            movie_title_list.append(text)
            # print(text)

    next_page = _html.find("div", attrs={'class': 'paginator'}).find(
        "span", attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_title_list, DOWNLOAD_URL + next_page['href']
    return movie_title_list, None

# 代码执行入口
def main():
    next_url = DOWNLOAD_URL
    with open('movie.txt', 'w') as f:
        while next_url:
            movies, next_url = parse_html(download_page_content(next_url))
            f.write(u'{movies}\n'.format(movies='\n'.join(movies)))


# resp.status_code
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(resp.content)
# pp.pprint(resp.encoding)
# pp.pprint(resp.json())

if __name__ == '__main__':
    main()
