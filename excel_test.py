#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-10
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import xlrd
import xlwt
import re
import csv

workbook = xlrd.open_workbook('file/20160128.xls')
# print 1, workbook.sheet_names()[0]  # 工作表1

# 获取整行和整列的值（数组）
sheet = workbook.sheets()[0]
# print 2, sheet.name, sheet.nrows, sheet.ncols  # 工作表1 28 10

# # 获取整行和整列的值（数组）
# '''
# 合并的行和列只算第一个行/列的值,其他的行和列为空!
# '''
# print 3, sheet.row_values(0)[0]
# print 4, sheet.row_values(1)[0]
#
# print 5, sheet.col_values(0)[0]
# print 6, sheet.col_values(1)[0]
#
# # 获取单元格内容,以下3种写法都可以!
# print 7, sheet.cell(1, 0).value.encode('utf-8')
# print 8, sheet.cell_value(1, 0).encode('utf-8')
# print 9, sheet.row(1)[0].value.encode('utf-8')

def set_style(name,height,bold=False):
  style = xlwt.XFStyle() # 初始化样式

  font = xlwt.Font() # 为样式创建字体
  font.name = name # 'Times New Roman'
  font.bold = bold
  font.color_index = 4
  font.height = height

  # borders= xlwt.Borders()
  # borders.left= 6
  # borders.right= 6
  # borders.top= 6
  # borders.bottom= 6

  style.font = font
  # style.borders = borders

  return style
trains_info = []
for i in range(0, sheet.nrows):
    sheet_col = sheet.cell(i, 0).value
    if u'日均定员' in sheet_col:
        value = sheet_col.encode('utf-8').split()
        trains_id = value[0]
        station = value[1]
        total = value[6]
        load_factors = value[-2]+'%'

        start_station = re.findall('(ZD.*?)—ZD', station)[0]
        final_station = re.findall('—([a-zA-z0-9-]+)', station)[0]
        trains_info.append([trains_id, '20160128', start_station, final_station, total, load_factors])
        print station, start_station, final_station, total, load_factors, sheet_col

table = xlwt.Workbook()
sheet1 = table.add_sheet('Shoufu')
row0 = ['车次','始发日期','起点站','终点站','日均定员','客座率']
# for i in range(0, len(row0)):
#     sheet1.write(0, i, row0[i], set_style(u'微软雅黑', 200, True))
# table.save('HEHEDA.xlsx')
writer = csv.writer(file('file/hehe.csv', 'wb'))
writer.writerow(row0)
for line in trains_info:
    writer.writerow(line)


def get_table_cols(sheet):
    for i in range(0, sheet.nrows):
        sheet_col = sheet.cell(i, 0).value
        if u'日均定员' in sheet_col:
            value = sheet_col.encode('utf-8').split()
            trains_id = value[0]
            station = value[1]
            total = value[6]
            load_factors = value[-2]+'%'

            start_station = re.findall('(ZD.*?)—ZD', station)[0]
            final_station = re.findall('—([a-zA-z0-9-]+)', station)[0]
            trains_info.append([trains_id, '20160128', start_station, final_station, total, load_factors])