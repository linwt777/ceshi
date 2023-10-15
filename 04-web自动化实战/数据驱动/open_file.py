# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/14 15:42
# @File:open_file.py

# f= open("aaa.txt",mode='r',encoding="UTF8")
#
# # print(f.readline())
# #
# # print(f.read())
#
# print(f.readlines())

# import csv
# c = csv.reader(open("aaa.csv","r",encoding="utf-8"))
# for cs in c :
#     print(cs)

# import xlrd
#
# xls = xlrd.open_workbook("aaa.xlsx")
#
# sheet = xls.sheet_by_index(0)
# #获取行数
# print(sheet.nrows)
# #获取列数
# print(sheet.ncols)
#
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

# json_str = open("aaa.json","r",encoding="utf8").read()
# print(json_str)
#
# import json
# #转成list格式
# json_ob = json.loads(json_str)
# print(json_ob)
# print(type(json_ob))
# print(json_ob[1][0]["name"])
# print('------------')
# #转会
# json2 = json.dumps(json_ob)
# print(type(json2))
# print(json.dumps(json2))

# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET
#
# tree = ET.parse("aaa.xml")
# root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)
#
# for chlid in root:
#     print(chlid.tag)
#     print(chlid.attrib)
#     print(chlid.text)
#     for children in chlid:
#         print(children.tag)
#         print(children.text)

import yaml
# yaml_str = "animal: pets"

yaml_str = open("aaa.yaml","r",encoding="utf8").read()

yaml_ob = yaml.load(yaml_str,Loader = yaml.FullLoader)
print(yaml_ob)