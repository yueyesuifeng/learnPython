# -*- coding: utf-8 -*-
# @Author: hewang
# @Date:   2018-01-22 17:34:29
# @Last Modified by:   hewang
# @Last Modified time: 2018-01-22 17:36:30
import os
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        for filename in files:
            if filename.startswith('WS') and filename.endswith('json'):
                print filename
        # print(files)  # 当前路径下所有非目录子文件

file_name("C:/refactor/prototype/web_gui/GUI/data")