from pyspark import SparkConf, SparkContext
from configparser import ConfigParser
from platform import python_revision
import pandas
import datetime
import re
import os
file = open('c:\AWS\config_file', 'r')
content = file.read()
paths = content.split("\n") #split it into lines
print(paths)
print(type(paths))
#print(paths.get("url"))

d={
    "url" : "UUUUU"
}
print(type(d))
print(d.get('url'))
print("++++++++++++++++++++++")
ll= []
dd = {}
for i in paths:
    if i.__contains__("="):
        ii = i.split('=')
        print(ii)
        dd[ii[0].translate({32: None})] = ii[1].translate({32: None})
#        print(dd)
print(dd)
print(dd.get('password1'))
print("++++++++++++++++++++++")

#    print(i)
#less_than_zero = filter(lambda x: "=" in x, paths)
#print(less_than_zero)
#parser = ConfigParser()
#parser.read('c:\AWS\config_file')
#print(parser.get('database_config', 'url'))
#print(parser.get('database_config', 'password1'))
d = {}
def Filter(datalist):
    # Search data based on regular expression in the list
    return [val for val in datalist
        if re.search(r'=', val)]
for b in Filter(paths):
   i = b.split('=')
   d[i[0]] = i[1]
#print(d)
Product_list = {x.translate({32: None}): y.translate({32: None})
                for x, y in d.items()}
print(Product_list)
print(Product_list['url'])
print(Product_list['username'])
print(Product_list['password1'])
i=10
b=20
print("even") if i%2==0 else print("odd")

os.curdir
