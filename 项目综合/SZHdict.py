'''
练习 ： 将单词本存入数据库

1. 创建数据库 dict  （utf8）
2. 创建数据表 words  将单词和单词解释分别存入不同的字段
3. 将单词存入words单词表  超过 19500 即可
'''

import pymysql
import re

f = open("dict.txt")#打开文件

# import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'dict_1',
                     charset = 'utf8')

cur = db.cursor()

sql = 'insert into works(work,mean) values (%s,%s)'
for line in f:
    #####获取单词和解释法一
    # lines = line.split(' ')
    # word = line[0]
    # mean = line[-1]
    # cur.execute(sql,(work, mean))
    # db.commit()
    ######或法二
    # data = f.readline()
    # tmp = data.split(' ')
    # word = tmp[0]
    # mean = ' '.join(tmp[1:]).strip()


    #获取单词和解释法三
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]#元祖 非空字符，匹配中间的空格，解释有些有无用点
    # print(tup)
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()



f.close()

cur.close()
db.close()

