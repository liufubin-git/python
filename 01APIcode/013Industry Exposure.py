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
filepath="E://01_api//Industry_Exposure.txt"
path="E://01_api//Industry_Exposure_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirties/HF0000000G%2CHF00000008/industry-style-exposure?endDate=2017-04-30"
data=get_api(url)
data=json.loads(data)
title=data.get("data").get("categories")
print len(data.get("data").get("dataset"))
# value_HF00000008=data.get("data").get("dataset")[0]
# value_HF00000008=value_HF00000008["values"]
# for i in range (0,len(data.get("data").get("dataset"))):
value1_HF00000008=data.get("data").get("dataset")[0]
id1_HF00000008=value1_HF00000008["id"]
alpha1_HF00000008=value1_HF00000008["alpha"]
dType1_HF00000008=value1_HF00000008["dType"]
value1_HF00000008=value1_HF00000008["values"]
# print  value1_HF00000008
value2_HF00000008=data.get("data").get("dataset")[1]
id2_HF00000008=value2_HF00000008["id"]
alpha2_HF00000008=value2_HF00000008["alpha"]
dType2_HF00000008=value2_HF00000008["dType"]
value2_HF00000008=value2_HF00000008["values"]
# print  value2_HF00000008
value3_HF0000000G=data.get("data").get("dataset")[2]
alpha3_HF0000000G=value3_HF0000000G["alpha"]
dType3_HF0000000G=value3_HF0000000G["dType"]
value3_HF0000000G=value3_HF0000000G["values"]
# print value3_HF0000000G
value4_HF0000000G=data.get("data").get("dataset")[3]
id4_HF0000000G=value4_HF0000000G["id"]
alpha4_HF0000000G=value4_HF0000000G["alpha"]
dType4_HF0000000G=value4_HF0000000G["dType"]
value4_HF0000000G=value4_HF0000000G["values"]
# print value4_HF0000000G

for i in range (0,len(title)):
    content="%-30s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-10s%-10s%-10s"%(title[i],id1_HF00000008,alpha1_HF00000008,dType1_HF00000008,dType2_HF00000008,value1_HF00000008[i],value2_HF00000008[i],id4_HF0000000G,alpha4_HF0000000G,dType3_HF0000000G,dType4_HF0000000G,value3_HF0000000G[i],value4_HF0000000G[i])
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