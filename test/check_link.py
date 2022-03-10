"""リンクにアクセスできるかを確認するスクリプト
"""

import sys
import traceback

import bs4
import markdown2
import requests

TARGET_PAGE = 'content/knowledge/index.md'


def check_link(target_link: str) -> None:
    """URL Linkの生存を確認する

    Args:
        target_link (str): 調査するサイトのURL
    """
    with open(target_link) as f:
        md = f.read()

    html = markdown2.Markdown().convert(md)
    soup = bs4.BeautifulSoup(html, "html.parser")

    # contentのclass属性を対象とする
    elems = soup.select('.content')

    href_list = []
    for i in elems[0].find_all("a"):
        if str(i).find("https") > 0:
            val_href = i.get("href")
            href_list.append(val_href)

    for i, href in enumerate(href_list):
        res_href = requests.get(href, allow_redirects=True, headers={'User-Agent': UA})
        if res_href.status_code != 200:
            raise ValueError(f"status code is {res_href.status_code}, check the URL link: {res_href.url}")
        else:
            print(f'href {i}, {href} : OK')


def main():
    # ターゲットページに対して，check_link関数を適用する
    try:
        check_link(TARGET_PAGE)

    except Exception as e:
        _, _, tb = sys.exc_info()
        raise ValueError(
            f'Exception error: {e} || Type: {str(type(e))} || Traceback Message: {traceback.format_tb(tb)}')


if __name__ == '__main__':
    main()
