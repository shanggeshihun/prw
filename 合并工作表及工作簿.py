# -*- coding: utf-8 -*-
"""
Created on 20190612

@author: dell
"""

"""========================
1. 将同一个Excel中的不同的sheet页，汇总到一个新的表格中
================================"""


import os
def file_name(file_dir):
    file_name_lst=[]
    for root,dirs,files in os.walk(file_dir):
        file_name_lst.extend(files)
    return file_name_lst
import xlrd
import xlsxwriter

main_path=r"C:\Users\dell\Desktop\已开票司机运单明细\天门分公司1月司机代征代缴数据\tiamen"
workbook_lst=file_name(main_path)

tar = []

# 遍历工作簿
for w in workbook_lst:
    w_path=main_path+"\\" + w
    data=xlrd.open_workbook(w_path)
    sheet_name_lst=data.sheet_names()
    sheet_name_lst=[n for n in sheet_name_lst if "运费_" in n]
    # 遍历工作表
    for sht in sheet_name_lst:
        sht_data=data.sheet_by_name(sht)
        nrows=sht_data.nrows
        # 遍历每一行
        for i in range(nrows):
            tar.append(sht_data.row_values(i))
            

#新建目标文件
tarfile=r"C:\Users\dell\Desktop\已开票司机运单明细\天门分公司1月司机代征代缴数据\tiamen.xlsx"
wh = xlsxwriter.Workbook(tarfile)
bold = wh.add_format({'bold':1})
wadd = wh.add_worksheet('total')
for row_num,row_data in enumerate(tar):
    wadd.write_row(row_num,0,row_data)
wh.close()
