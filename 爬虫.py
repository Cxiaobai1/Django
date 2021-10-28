import requests
from lxml import etree
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    port=3306,
    database='bookstore',
)
cursor = db.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

url = 'https://yuedu.163.com/book/rank/free/all/p'

for i in range(1, 6):
    url_new = url + str(i) + '/s20'
    response = requests.get(headers=headers, url=url_new)
    res_html = etree.HTML(response.text)
    title = res_html.xpath('//div[@class="tab-item clearfix"]/div/a/h2/text()')
    author = res_html.xpath('//div[@class="tab-item clearfix"]/div/a/p/text()')
    desc = res_html.xpath('//div[@class="tab-item clearfix"]/div/a/div/p/text()')
    image_url = res_html.xpath('//div[@class="tab-item clearfix"]/div/a/img/@src')
    # print(title,author,desc,image_url)
    for title, author, desc, image_url in zip(title, author, desc, image_url):
        # print(title)
        sql = 'insert into index_allbook(title,author,description,img_ul) values (%s,%s,%s,%s)'
        cursor.execute(sql, [title, author, desc, image_url])
        db.commit()
cursor.close()
db.close()
