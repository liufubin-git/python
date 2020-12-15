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
filepath="E://01_api//Historical_Asset_Exposure.txt"
path="E://01_api//Historical_Asset_Exposure_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirties/HF00001F16/historical-asset-style-exposure?startDate=2017-01-01&endDate=2017-06-10&index=ManagedFuture"
data=get_api(url)
data=json.loads(data)
title=data.get("data").get("categories")
s=len(data.get("data").get("dataset"))
print len(title),s

for i in range (0,s):
    name=data.get("data").get("dataset")[i]["name"]
    adata=data.get("data").get("dataset")[i]["data"]
    content="%-10s%-50s"%(name,adata)
    print content
    writetxt(filepath,content)
    writetxt(filepath, "\n")
title= "date%s"%(title)
print title
writetxt(filepath, title)
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