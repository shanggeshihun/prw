# -*- coding: utf-8 -*-
"""
Created on 20190408
1 判断文件夹是否存在
"""
import datetime
import os

today=datetime.date.today()
yesterday=today-datetime.timedelta(days=0)
yesterday=datetime.date.strftime(yesterday,'%Y%m%d')
partPath="C:\\Users\\dell\\Desktop\\"
Path=partPath+str(yesterday)+".txt"
existFlag=os.path.exists(Path)
print(existFlag)


import time
import pandas as pd
import pymysql
import sqlalchemy
import numpy as np
import json
import datetime
import os

