# -*- coding: utf-8 -*-

import json, os


def get_cms_data():
    '''
    打开指纹数据文件，读取数据返回
    '''
    path = os.getcwd()
    with open(path + "/cms_data/data.json", "r", encoding="utf-8") as f:
        datas = json.load(f, encoding="utf-8")
        re_data = []
        md5_data = []
        for data in datas:
            if data["re"] != "":
                re_data.append(data)
            else:
                md5_data.append(data)
        return re_data, md5_data
