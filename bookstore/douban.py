import requests
from lxml import etree
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='',
                       database='bookstore',
                       charset='utf8')
cursor = conn.cursor()

# wb = Workbook()
# ws = wb.active
# ws.append(['书名', '作者', '图片链接', '简介'])

url = 'https://yuedu.163.com/book/rank/free/month/p'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

for i in range(1, 6):
    url_t = url + str(i) + '/s20'
    response = requests.post(headers=headers, url=url_t)
    res = response.text
    etree_res = etree.HTML(res)
    # etree_str = etree.tostring(etree_res, encoding='utf-8')
    # print(etree_str.decode())
    res_author = etree_res.xpath('//div[@class="tab-item clearfix"]/div/a/p/text()')
    res_title = etree_res.xpath('//div[@class="tab-item clearfix"]/div/a/h2/text()')
    res_img = etree_res.xpath('//div[@class="tab-item clearfix"]/div/a/img/@src')
    res_desc = etree_res.xpath('//div[@class="tab-item clearfix"]/div/a/div/p/text()')
    res_num = etree_res.xpath('//div[@class="tab-item clearfix"]/div/div/text()')

    for author, title, img_url, desc, num in zip(res_author, res_title, res_img, res_desc, res_num):
        # print(num)
        sql = "insert into index_mfbook (title, author, description, img_ul, num) values(%s, %s, %s, %s, %s);"
        cursor.execute(sql, [title, author, desc, img_url, num])
        # sql = "insert into index_allbook (title, author, description, img_ul) values(%s, %s, %s, %s);"
        # cursor.execute(sql, [title, author, desc, img_url])
        conn.commit()
    print("第%s页写入数据库成功" % i)
cursor.close()
conn.close()
