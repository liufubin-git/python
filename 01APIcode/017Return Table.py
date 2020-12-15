#coding=utf-8
import urllib2,json,ssl,re,time,os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def get_api(url):
    context=ssl._create_unverified_context()  #创建一个未验证的证书
    req = urllib2.Request(url) #定义请求信息，其中可以包含参数
    res = urllib2.urlopen(req,context=context) #打开一个请求
    data = res.read() #读取服务器的返回数据
    return data

# def ip_address(ip):
#     url=ip_url(ip)
#     data=get_api(url)
#     data=json.loads(data.decode("gbk"))
#     ipdata=data.get("data")
#     return ipdata[0].get("location")

def writetxt(filepath,content):
    if os.path.isfile(filepath):
        infofile=open(filepath,"a")
    elif os.path.isdir(os.path.split(filepath)[0]):
        infofile = open(filepath, "w")
    else:
        os.makedirs(os.path.split(filepath)[0])
        infofile=open(filepath,"w")
    infofile.write(content)
    infofile.close()

def readtext(filepath):
    infofile=open(filepath,"r")
    content=infofile.readlines()
    infofile.close()
    return content
#120.77.57.67
filepath="E://01_api//Return_Table.txt"
path="E://01_api//Return_Table_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirty/HF0000000G%2CHF00000008/investment-historical-return?frequency=Monthly&startDate=2016-01-01&endDate=2017-06-01"
data=get_api(url)
data=json.loads(data)
s=len(data.get("data").get("data"))
print s
datetime=data.get("data").get("datetime")
print datetime
for i in range (0,s):
    year=data.get("data").get("data")[i]["year"]
    rets=data.get("data").get("data")[i]["rets"]
    content="%-10s%-10s"%(year,rets)
    print content
    writetxt(filepath, content)
    writetxt(filepath, "\n")
datetime="datetime%s"%(datetime)
writetxt(filepath, datetime)
writetxt(filepath, "\n")
content1=readtext(filepath)
content2=readtext(path)
# print content1  ,"\n"
# print content2
if content1==content2:
    print "数据相等"
else:
    print "接口出错"
os.remove(filepath)