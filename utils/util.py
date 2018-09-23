#coding = utf-8

"""
@author: sy

@file: util.py

@time: 2018/9/23 20:54

@desc: 工具

"""

import os


# 读取
def read_cmd():
    # 获取key文件的绝对路径
    cmd_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cmd')
    with open(cmd_path, 'r', encoding='utf-8') as f:
        cmd = f.read()
        f.close()
    return cmd