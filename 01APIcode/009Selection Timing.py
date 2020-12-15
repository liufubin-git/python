#coding=utf-8
import urllib2,json,ssl,re,time,os

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
filepath="E://01_api//Selection_Timing.txt"
path="E://01_api//Selection_Timing_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirties/HF00000008%2CHF0000000G/selection-timing?startDate=2015-01-01&endDate=2017-05-01&skill=Selection"
data=get_api(url)
data=json.loads(data)
date=data.get("data").get("categories")
value_HF00000008=data.get("data").get("dataset")[0]
value_HF00000008=value_HF00000008["values"]
value_HF0000000G=data.get("data").get("dataset")[1]
value_HF0000000G=value_HF0000000G["values"]
# print value_HF00000008
# print value_HF0000000G
for i in range (0,len(date)):
    content="%-10s%-5s%-5s"%(date[i],value_HF00000008[i],value_HF0000000G[i])
    writetxt(filepath,content)
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