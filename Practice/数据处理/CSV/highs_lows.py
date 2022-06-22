import csv
from matplotlib import pyplot as plt
from datetime import datetime


#filename = 'E:\浏览器下载\Python课程\程序代码\Practice\数据处理\CSV\data\sitka_weather_07-2014.csv'
#filename = 'E:\浏览器下载\Python课程\程序代码\Practice\数据处理\CSV\data\sitka_weather_2014.csv'
filename = 'E:\浏览器下载\Python课程\程序代码\Practice\数据处理\CSV\data\death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
     
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)              
            highs.append(high)     
            lows.append(low)


# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(8, 6))
#实参alpha 指定颜色的透明度。Alpha 值为0表示完全透明，1（默认设置）表示完全不透明.
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
#给图表区域着色,使用方法fill_between() ，它接受一个 x 值系列和两个 y 值系列，并填充两个 y 值系列之间的空间
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# 设置图形的格式
plt.title("Daily high and low temperatures--2014\nDeath Valley, CA", fontsize=16)
plt.xlabel('', fontsize=10)

#绘制斜的日期标签
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

    