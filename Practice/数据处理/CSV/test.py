import csv

#filename = 'E:\浏览器下载\Python课程\程序代码\Practice\数据处理\CSV\data\sitka_weather_07-2014.csv'
filename = 'E:\浏览器下载\Python课程\程序代码\Practice\数据处理\CSV\data\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        print(row)