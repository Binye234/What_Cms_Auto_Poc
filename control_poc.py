# -*- coding: utf-8 -*-

from pocs import *


class control:
    '''
    POC控制类
    '''

    def __init__(self, poc_db, cms_mode):
        self.poc_db = poc_db
        self.cms_mode = cms_mode

    def search(self, cms):
        '''
        根据关键字搜索POC
        :return:
        '''
        for value in self.poc_db.data.values():
            for key in value.keys():
                if key.find(cms)>=0:
                    print(f"[+]{key}")


    def auto_poc(self):
        '''
        根据CMS的类型自动加载相应的POC
        :return:
        '''
        if self.cms_mode.type not in self.poc_db.data.keys():
            print("CMS类型不支持")
            return
        for key in self.poc_db.data.keys():
            if self.cms_mode.type == key:
                for value in self.poc_db.data[key].values():
                    exec(value)
                return
