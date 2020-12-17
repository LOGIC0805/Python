import pandas as pd
import datetime
from time import sleep
datas = pd.read_csv('stuGrade.csv')
num = len(datas)
sum_chinese = sum(datas['chinese'])
mean_chinese = sum_chinese / num
sum_math = sum(datas['math'])
mean_math = sum_math / num
sum_english = sum(datas['english'])
mean_english = sum_english / num
print('语文平均成绩：%.2f' % mean_chinese)
print('数学平均成绩：%.2f' % mean_math)
print('英语平均成绩：%.2f' % mean_english)
with open('my.txt', 'w+') as filename:
    filename.write('10185101165 崔鹏宇\n')
    filename.write('%.2f, %.2f, %.2f\n' %(mean_chinese, mean_math, mean_english))
    filename.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    sleep(2)
    filename.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')