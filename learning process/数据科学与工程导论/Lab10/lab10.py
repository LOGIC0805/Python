import pymysql
import csv
import pandas as pd
import matplotlib.pyplot as plt

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com",  port = 10209, user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()
sql = "SELECT * FROM SH_Grade;"
cursor.execute(sql)
results = cursor.fetchall()
datas = []
for result in results:
    data = list(result)
    dataclass = data[1][0]
    data.insert(2, dataclass)
    datas.append(data)
titles = ['id','StuId','Class','Sex']
for grade in range(6, 10):
    if grade < 8:
        titles.append('CHI' + str(grade) + '11')
        titles.append('MATH' + str(grade) + '11')
        titles.append('ENG' + str(grade) + '11')
        titles.append('CHI' + str(grade) + '12')
        titles.append('MATH' + str(grade) + '12')
        titles.append('ENG' + str(grade) + '12')
        titles.append('CHI' + str(grade) + '21')
        titles.append('MATH' + str(grade) + '21')
        titles.append('ENG' + str(grade) + '21')
        titles.append('CHI' + str(grade) + '22')
        titles.append('MATH' + str(grade) + '22')
        titles.append('ENG' + str(grade) + '22')
    elif grade == 8:
        titles.append('CHI' + str(grade) + '11')
        titles.append('MATH' + str(grade) + '11')
        titles.append('ENG' + str(grade) + '11')
        titles.append('PHY' + str(grade) + '11')
        titles.append('CHI' + str(grade) + '12')
        titles.append('MATH' + str(grade) + '12')
        titles.append('ENG' + str(grade) + '12')
        titles.append('PHY' + str(grade) + '12')
        titles.append('CHI' + str(grade) + '21')
        titles.append('MATH' + str(grade) + '21')
        titles.append('ENG' + str(grade) + '21')
        titles.append('PHY' + str(grade) + '21')
        titles.append('CHI' + str(grade) + '22')
        titles.append('MATH' + str(grade) + '22')
        titles.append('ENG' + str(grade) + '22')
        titles.append('PHY' + str(grade) + '22')
    elif grade == 9:
        titles.append('CHI' + str(grade) + '11')
        titles.append('MATH' + str(grade) + '11')
        titles.append('ENG' + str(grade) + '11')
        titles.append('PHY' + str(grade) + '11')
        titles.append('CHE' + str(grade) + '11')
        titles.append('CHI' + str(grade) + '12')
        titles.append('MATH' + str(grade) + '12')
        titles.append('ENG' + str(grade) + '12')
        titles.append('PHY' + str(grade) + '12')
        titles.append('CHE' + str(grade) + '12')
        titles.append('CHI' + str(grade) + '21')
        titles.append('MATH' + str(grade) + '21')
        titles.append('ENG' + str(grade) + '21')
        titles.append('PHY' + str(grade) + '21')
        titles.append('CHE' + str(grade) + '21')
with open('SH_Grade.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(titles)
    for data in datas:
        writer.writerow(data)

datas = pd.read_csv('SH_Grade.csv')
print('条目数量: ', datas.shape[0])
datas = datas.drop_duplicates('StuId')
print('条目数量: ', datas.shape[0])
datas = datas.dropna(thresh = datas.shape[1] - 12)
print('条目数量: ', datas.shape[0])
datas.Sex = datas.Sex.fillna(method = 'ffill')
for col in datas.columns[datas.isnull().any()].tolist():
    datas[col] = datas[col].fillna(datas[col].median())
for col in datas.columns.tolist()[4:]:
    print(col, datas[col].max())
datas.CHI822 = datas.CHI822 / 120 * 100
datas.MATH822 = datas.MATH822 / 120 * 100
datas.ENG822 = datas.ENG822 / 120 * 100
datas.CHI911 = datas.CHI911 / 150 * 100
datas.MATH911 = datas.MATH911 / 150 * 100
datas.ENG911 = datas.ENG911 / 150 * 100
datas.PHY911 = datas.PHY911 / 90 * 100
datas.CHE911 = datas.CHE911 / 60 * 100
datas.CHI912 = datas.CHI912 / 150 * 100
datas.MATH912 = datas.MATH912 / 150 * 100
datas.ENG912 = datas.ENG912 / 150 * 100
datas.CHI921 = datas.CHI921 / 150 * 100
datas.MATH921 = datas.MATH921 / 150 * 100
datas.ENG921 = datas.ENG921 / 150 * 100
datas.PHY921 = datas.PHY921 / 90 * 100
datas.CHE921 = datas.CHE921 / 60 * 100

female = datas.loc[datas['Sex'] == 'F'].groupby('Class')['Sex'].count()
male = datas.loc[datas['Sex'] == 'M'].groupby('Class')['Sex'].count()
plt.bar(female.index, female.values, label = 'female')
plt.bar(male.index, male.values, bottom = female.values, label = 'male')
plt.legend()
plt.show()
A13 = datas.loc[datas['StuId'] == 'A13']
A13_course = []
A13_grades = []
for course in A13.columns.tolist()[4:]:
    if 'CHI' in course:
        A13_course.append(course[3:])
        A13_grades.append(A13[course].values[0])
A15 = datas.loc[datas['StuId'] == 'A15']
A15_course = []
A15_grades = []
for course in A13.columns.tolist()[4:]:
    if 'CHI' in course:
        A15_course.append(course[3:])
        A15_grades.append(A15[course].values[0])
plt.plot(A13_course, A13_grades, label = 'A13')
plt.plot(A15_course, A15_grades, label = 'A15')
plt.xlabel('CHI')
plt.ylabel('Percentile Grages')
plt.legend()
plt.show()

result1 = datas.loc[(datas['CHI721'] < 60) | (datas['ENG721'] < 60)].loc[:, ['StuId', 'Class', 'CHI721', 'ENG721']]
print(result1)
result1.to_csv('task8.csv')
result2 = datas.loc[(datas['Class'] == 'A') | (datas['Class'] == 'C')].loc[:, ['Class', 'CHI622', 'MATH622', 'ENG622']]
print(result2.groupby('Class').agg(['mean', 'var']))
print('在6年级第2学期期末考试中：A班的语文平均成绩比C班高，并且两个班的语文成绩分布差别不大；A班C班的数学平均成绩差别不大，但是A班的数学成绩分布比较平稳，优等生和差生成绩差别不大，而C班优等生和差生数学成绩差别很大，水平趋于两极分化；A班C班英语平均成绩也差别不大，并且分布也差别不大。')