#测试用压缩的数据
import re
from typing import List
from urllib.request import Request, urlopen
import gzip,zlib
import json,tkinter,turtle

#网站获取数据Api
url = 'http://t.weather.sojson.com/api/weather/city/101250101'
#包装头部
firefox_headers = {'User-Agent': "	Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0 " , "Accept-Encoding" :"gzip, deflate"}

#构建请求
request = Request( url, headers=firefox_headers )
html = urlopen( request )



#获取数据以utf-8的编码方式
#data2 = html.read().decode('utf-8')
data2 = zlib.decompress(html.read(), 16+zlib.MAX_WBITS).decode('utf-8')
data1=str(data2)
# 将json数据转换为dict数据
weather_dict=json.loads(data2)
#data3 =dict(html.read().decode('utf-8'))
#data3 =dict (str(data2))

#print(weather_dict)
forecast = weather_dict.get('data').get('forecast')
'''
print('城市：', weather_dict.get('cityInfo').get('parent')+' '+weather_dict.get('cityInfo').get('city'))
print('更新时间：', weather_dict.get('cityInfo').get('updateTime'))
print('温度：', weather_dict.get('data').get('wendu') + '℃ ')
print('空气质量：', weather_dict.get('data').get('quality'))
print('风向：', forecast[0].get('fx'))
print('风向：', weather_dict.get('data').get('forecast')[0].get('fx'))
'''


t_d = [str(str([weather_dict.get('data').get('yesterday').get('ymd')])[7:-2])]
t_h = [int(str([weather_dict.get('data').get('yesterday').get('high')])[5:-3])]
#t_t  = (str([weather_dict.get('data').get('yesterday').get('low')])[0:])
t_l = [int(str([weather_dict.get('data').get('yesterday').get('low')])[5:-3])]



for i in range(1,16,1):
    t_d.insert(i, str(str([forecast[i - 1].get('ymd')])[7:-2]))
    t_h.insert(i, int(str([forecast[i - 1].get('high')])[5:-3]))
    t_l.insert(i, int(str([forecast[i - 1].get('low')])[5:-3]))
#    t_l.insert(i, forecast[i - 1].get(str([weather_dict.get('data').get('yesterday').get('low' )])[3:-3]))
#    t_l.insert(i, forecast[i - 1].get('low'))

#计算半月最高温与最低温的差值与平均值，比以平均值作为0线画图
chazhi=max(t_h)-min(t_l)
pingjun=int(max(t_h)-chazhi/2)

'''
print(t_h)
print(t_l)
print(pingjun)
'''
#预猜测半月最大温差50度

'''
for i in range(0, 16, 1):
#    print(i)
    print(t_d[i]+'\t'+str(t_h[i])+'\t'+str(t_l[i]))
    print('\n')
'''

#海龟制图默认为300*300的方形
#绘制网格线，X轴为日期轴差值为20，Y轴为温度轴差值为6
#turtle.bgcolor('gray')
turtle.speed(0)
turtle.width(1)
turtle.color('gray')
turtle.penup()
#更改起始位置
turtle.goto(300, 300)
for x in range(0,51,1):
#    turtle.goto(-300, 300 - x * 12)
    turtle.color('red')
    turtle.goto(-305, 290 - x * 12)
    turtle.write(pingjun+25-x,align='right',font=('arial',6,'normal'))
    turtle.goto(-300, 300 - x * 12)
    turtle.color('gray')
    turtle.pendown()
    turtle.goto( 300, 300 - x * 12)
    turtle.penup()


for y in range(0,16,1):
#    turtle.goto(-300+y*40, 300)
    turtle.color('red')
    turtle.goto(-310 + y * 40, 300)
    turtle.write(t_d[y],font=('arial',6,'normal'))
    turtle.goto(-300 + y * 40, 300)
    turtle.color('gray')
    turtle.pendown()
    turtle.goto(-300+y*40, -300)
    turtle.penup()


#我以X轴-300为昨日的坐标位，300为15日后的坐标位
#我以Y轴-300为零下50°的坐标，300为正50度的坐标

#高温曲线
turtle.speed(10)
turtle.width(5)
turtle.color('blue')
turtle.penup()
for p in range(0,16,1):
    turtle.goto(-300+40*p, (t_h[p]-pingjun) * 6)
    turtle.pendown()
#低温曲线
turtle.color('LightBlue')
turtle.penup()
for p in range(0,16,1):
    turtle.goto(-300+40*p, (t_l[p]-pingjun) * 6)
    turtle.pendown()






turtle.done()


#os.system('pause')

#turtle.mainloop()



