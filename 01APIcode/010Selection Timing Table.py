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
filepath="E://01_api//Selection_Timing_Table.txt"
path="E://01_api//Selection_Timing_Table_1.txt"

url="http://120.77.57.67:8080/dataservice/v1/secuirty/HF0000000G/selection-timing-table?endDate=2017-04-30"
data=get_api(url)
data=json.loads(data)
title=data.get("data").get("categories")
# value_HF00000008=data.get("data").get("dataset")[0]
# value_HF00000008=value_HF00000008["values"]
# for i in range (0,len(data.get("data").get("dataset"))):
value1_HF0000000G=data.get("data").get("dataset")[0]  #成立以来的数据
id1_HF0000000G=value1_HF0000000G["id"]
value1_HF0000000G=value1_HF0000000G["values"]
# print id1_HF0000000G, value1_HF0000000G
value2_HF0000000G=data.get("data").get("dataset")[1]  #最近2年的数据
id2_HF0000000G=value2_HF0000000G["id"]
value2_HF0000000G=value2_HF0000000G["values"]
# print id2_HF0000000G, value2_HF0000000G
value3_HF0000000G=data.get("data").get("dataset")[2]  #最近3年的数据
id3_HF0000000G=value3_HF0000000G["id"]
value3_HF0000000G=value3_HF0000000G["values"]
# print id3_HF0000000G, value3_HF0000000G
value4_HF0000000G=data.get("data").get("dataset")[3]  #最近4年的数据
id4_HF0000000G=value4_HF0000000G["id"]
value4_HF0000000G=value4_HF0000000G["values"]
# print id4_HF0000000G, value4_HF0000000G
value5_HF0000000G=data.get("data").get("dataset")[4]  #最近5年的数据
id5_HF0000000G=value5_HF0000000G["id"]
value5_HF0000000G=value5_HF0000000G["values"]
# print id5_HF0000000G, value5_HF0000000G

for i in range (0,len(title)):
    content="%-20s%-20s%-20s%-20s%-20s%-20s%-20s"%(title[i],id1_HF0000000G,value1_HF0000000G[i],value2_HF0000000G[i],value3_HF0000000G[i],value4_HF0000000G[i],value5_HF0000000G[i])
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