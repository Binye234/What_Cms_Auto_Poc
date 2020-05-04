# -*- coding: utf-8 -*-

from cms_data.get_cms_data import *
import hashlib, requests, threading
from find_cms.cms_enum import *
from find_cms.cms_model import *

'''
class re_find(threading.Thread):
   
    def __init__(self, cms_model, cms_data):
        super.__init__()
        self.cms_mode = cms_model
        self.cms_data = cms_data

    def get_cms_url(self):
       
        try:
            response = requests.get(self.cms_mode.url + self.cms_data["url"], timeout=5)
            if response.status_code == 200:
                return response.text
            return None
        except:
            return None

    def run(self):
        if self.cms_mode.flag:
            return
        text = get_cms_data()
        if text:
            return
        if self.cms_data["re"] in text:
            self.cms_mode.name = self.cms_data["name"]
            self.cms_mode.flag = True

'''


class CmsScanner:
    '''cms自动化检测类'''

    def __init__(self, cms_mode):
        data = get_cms_data()
        self.re_Data = data[0]
        self.md5_data = data[1]
        self.cms_mode = cms_mode  # 以模型传递值
        self.flag = False  # 判断是否找到类型

    def get_cms_url(self, url):
        '''网络请求方法'''
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
            response = requests.get(self.cms_mode.url + url, headers=headers,
                                    timeout=5)
            if response.status_code == 200:
                return response.text
            return None
        except:
            return None

    def re_find(self, name, re, url):

        text = self.get_cms_url(url)
        if text == None:
            return
        if re in text:
            self.cms_mode.name = name
            self.flag = True

    def md5_find(self, name, md5, url):
        '''文件md5值查找'''
        text = self.get_cms_url(url)
        if text == None:
            return
        if md5 == hashlib.md5(text.encode("utf-8")).hexdigest():
            self.cms_mode.name = name
            self.flag = True

    def cms_type(self):
        '''查找类型枚举'''
        for cms_t in Cms_Enum:
            if cms_t.value == self.cms_mode.name:
                self.cms_mode.type = cms_t
                break

    def run(self):
        find_list = []
        for mode in self.re_Data:
            if self.flag:
                break
            task = threading.Thread(target=self.re_find, args=(mode["name"], mode["re"], mode["url"]))
            find_list.append(task)
            task.start()
        for mode in self.md5_data:
            if self.flag:
                break
            task = threading.Thread(target=self.md5_find, args=(mode["name"], mode["md5"], mode["url"]))
            find_list.append(task)
            task.start()
        for task in find_list:
            task.join()
        if self.cms_mode.name != "":
            self.cms_type()
