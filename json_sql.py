# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:37:43 2019

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:03:02 2019

连接数据库，解析json字段，重新存入数据库
"""
#coding:utf-8
import json
import time
#字典》(key,value)

#对json文件分别解析成 字典长度 关键字列表 值列表
def str_to_dic(string):
#    t=('{"晋BA7687":"1","晋F03316":"1"}',)
    dic=json.loads(string)
    dic_len=len(dic)
    k_lst=[]
    v_lst=[]
    for k in dic.keys():
        k_lst.append(k)
        v_lst.append(dic[k])
    return dic_len,k_lst,v_lst,

import pymysql

#清洗日期,表名,表的关键字名，表的json字段名，关键字值，k 值 ，v值
def json_into_lst(etl_date,tb_name,primary_key_name,json_field_name):
    h='192.168.0.204'
    p=6612
    u='bi'
    pw='79f6ba05a7e0bbb7dbcc4cc2fbdb15c9'
    d='odm'

    repeat_etl_date_f=[]
    repeat_tb_name_f=[]
    repeat_primary_key_name_f=[]
    repeat_json_field_name_f=[]
    repeat_id_f=[]
    k_lst_f=[]
    v_lst_f=[]
    
    conn=pymysql.Connect(host=h,port=p,user=u,passwd=pw,db=d,charset='utf8')
    cursor=conn.cursor()
    #从数据库读取表
    conn=pymysql.Connect(host=h,port=p,user=u,passwd=pw,db=d,charset='utf8')
    cursor=conn.cursor()
    #    查询返回结果是tuple
    read_tb="select {0},{1} from {2} where sjb_etl_date='{3}'".format(primary_key_name,json_field_name,tb_name,etl_date)
    cursor.execute(read_tb)
    vehicle_labs_result=cursor.fetchall()
    for each in vehicle_labs_result:
        repeat_etl_date=[]
        repeat_tb_name=[]
        repeat_primary_key_name=[]
        repeat_json_field_name=[]
        
        repeat_id=[]
        each_str=each[1]
        if each_str:
            try:
                str_to_dic(each_str)
            except:
                continue
            else:
                dic_len,k_lst,v_lst=str_to_dic(each_str)
                [repeat_etl_date.append(etl_date) for i in range(dic_len)]
                [repeat_tb_name.append(tb_name) for i in range(dic_len)]
                [repeat_primary_key_name.append(primary_key_name) for i in range(dic_len)]
                [repeat_json_field_name.append(json_field_name) for i in range(dic_len)]
                [repeat_id.append(each[0]) for i in range(dic_len)]
    
                repeat_etl_date_f.extend(repeat_etl_date)
                repeat_tb_name_f.extend(repeat_tb_name)
                repeat_primary_key_name_f.extend(repeat_primary_key_name)
                repeat_json_field_name_f.extend(repeat_json_field_name)
                repeat_id_f.extend(repeat_id)
                k_lst_f.extend(k_lst)
                v_lst_f.extend(v_lst)
    return repeat_etl_date_f,repeat_tb_name_f,repeat_primary_key_name_f,repeat_json_field_name_f,repeat_id_f,k_lst_f,v_lst_f


#写入数据库
def lst_to_sql(data):
    h='192.168.0.204'
    p=6612
    u='bi'
    pw='79f6ba05a7e0bbb7dbcc4cc2fbdb15c9'
    d='repm'

    conn=pymysql.Connect(host=h,port=p,user=u,passwd=pw,db=d,charset='utf8')
    cursor=conn.cursor()
    
    # r=len(data[0])
    r=2000
    print(r)
    for i in range(r):
        insert_sql="insert into json_into_temp_remp_table values({0},{1},{2},{3},{4},{5},{6})"
        sql=insert_sql.format("'"+data[0][i]+"'",
                              "'"+data[1][i]+"'",
                              "'"+data[2][i]+"'",
                              "'"+data[3][i]+"'",
                              "'"+data[4][i]+"'",
                              "'"+data[5][i]+"'",
                              "'"+data[6][i]+"'"
                              )
#        print(sql)
#        cursor.execute(sql)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    cursor.close()
    conn.close()


if __name__=='__main__':
    t=time.time()
    etl_date="2019-03-05"
    tb_name="fs_bam_bams_driver_cert_templet_his"
    primary_key="id"
    json_field="templet_label"
#    json_field="templet_content"
#    json_field="vehicle_labs"
    data=json_into_lst(etl_date,tb_name,primary_key,json_field)
    lst_to_sql(data)
    print(json_field,time.time()-t)