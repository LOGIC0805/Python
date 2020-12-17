import pymysql
import numpy as np

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com",  port = 10209, user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()

sql = "SELECT * FROM bicycle_train LIMIT 17,5;"
cursor.execute(sql)
result = cursor.fetchall()
print("1. 从第18条记录开始的5条记录")
for data in result:
    print(data)

sql = "SELECT MAX(wind) FROM bicycle_train;"
cursor.execute(sql)
max = cursor.fetchone()
sql = "SELECT MIN(wind) FROM bicycle_train;"
cursor.execute(sql)
min = cursor.fetchone()
print("2. 数据表中风级(wind)取值范围")
print(min[0], '~', max[0])

sql = "SELECT AVG(temp_air) FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND wind<=1 AND y>=100;"
cursor.execute(sql)
result = cursor.fetchone()
print("3. 满足城市为北京市，10时，晴天，无风或1级风，租用单车数量不小于100条件下大气温度的平均值")
print(result[0])

sql = "SELECT temp_air FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND wind<=1 AND y>=100;"
cursor.execute(sql)
result = cursor.fetchall()
datas = []
for data in result:
    datas.append(data[0])
print("4. 满足城市为北京市，10时，晴天，无风或1级风，租用单车数量不小于100条件下大气温度的方差")
print(np.var(datas))

sql = "SELECT city, SUM(y) FROM bicycle_train WHERE weather=3 AND is_workday=1 GROUP BY city ORDER BY SUM(y) DESC;"
cursor.execute(sql)
result = cursor.fetchall()
print("5. 分城市显示工作日雨雪天单车租用总量，并降序排序")
for data in result:
    strresult = '上海'
    if data[0] == 1:
        strresult = '北京'
    strresult += '：'
    print(strresult, data[1])

sql = "SELECT hour, AVG(y) FROM bicycle_train WHERE is_workday=1 AND city=1 AND temp_body<=10 AND hour>=17 AND hour<=19 GROUP BY hour ORDER BY hour;"
cursor.execute(sql)
result = cursor.fetchall()
print("6. 分别查询17时至19时每小时上海市在工作日且体感温度不大于10摄氏度时租用单车的平均值（四舍五入至整数），并且结果按时间升序排序")
for data in result:
    print(data[0], '时', round(data[1], 0), '辆')
