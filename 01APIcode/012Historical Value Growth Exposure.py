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
filepath="E://01_api//Historical_Value_Growth_Exposure.txt"
path="E://01_api//Historical_Value_Growth_Exposure_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirties/HF0000000G%2CHF00000008/historical-value-growth-style-exposure?startDate=2017-01-01&endDate=2017-04"
data=get_api(url)
data=json.loads(data)
date=data.get("data").get("categories")
s=len(data.get("data").get("dataset"))
print s
# value_HF00000008=data.get("data").get("dataset")[0]
# value_HF00000008=value_HF00000008["values"]
# for i in range (0,len(data.get("data").get("dataset"))):
value1_HF00000008=data.get("data").get("dataset")[0]
name1_HF00000008=value1_HF00000008["name"]
value1_HF00000008=value1_HF00000008["data"]
# print  value1_HF00000008
value2_HF00000008=data.get("data").get("dataset")[1]
name2_HF00000008=value2_HF00000008["name"]
value2_HF00000008=value2_HF00000008["data"]
# print  value2_HF00000008
value3_HF00000008=data.get("data").get("dataset")[2]
name3_HF00000008=value3_HF00000008["name"]
value3_HF00000008=value3_HF00000008["data"]
# print value3_HF0000000G
value4_HF00000008=data.get("data").get("dataset")[3]
name4_HF00000008=value4_HF00000008["name"]
value4_HF00000008=value4_HF00000008["data"]
# print value4_HF0000000G
value5_HF00000008=data.get("data").get("dataset")[4]
name5_HF00000008=value5_HF00000008["name"]
value5_HF00000008=value5_HF00000008["data"]
# print value4_HF0000000G
value6_HF00000008=data.get("data").get("dataset")[5]
name6_HF00000008=value6_HF00000008["name"]
value6_HF00000008=value6_HF00000008["data"]
# print value4_HF0000000G
value7_HF00000008=data.get("data").get("dataset")[6]
name7_HF00000008=value7_HF00000008["name"]
value7_HF00000008=value7_HF00000008["data"]
# print value4_HF0000000G

for i in range (0,len(date)):
    content="%-20s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s"%(date[i],name1_HF00000008,value1_HF00000008[i],name2_HF00000008,value2_HF00000008[i],name3_HF00000008,value3_HF00000008[i],name4_HF00000008,value4_HF00000008[i],name5_HF00000008,value5_HF00000008[i],name6_HF00000008,value6_HF00000008[i],name7_HF00000008,value7_HF00000008[i])
    print content
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