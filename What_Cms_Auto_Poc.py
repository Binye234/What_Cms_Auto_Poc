# -*- coding: utf-8 -*-

from find_cms import *
from pocs import poc_db
import requests
import control_poc
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logo = '''
__        ___           _       ____                      _         _        
\ \      / / |__   __ _| |_    / ___|_ __ ___  ___       / \  _   _| |_ ___  
 \ \ /\ / /| '_ \ / _` | __|  | |   | '_ ` _ \/ __|     / _ \| | | | __/ _ \ 
  \ V  V / | | | | (_| | |_   | |___| | | | | \__ \    / ___ \ |_| | || (_) |
   \_/\_/  |_| |_|\__,_|\__|___\____|_| |_| |_|___/___/_/   \_\__,_|\__\___/ 
                          |_____|                |_____|                     
      ____            
     |  _ \ ___   ___ 
     | |_) / _ \ / __|
     |  __/ (_) | (__ 
 ____|_|   \___/ \___|
|_____|  

自动识别目标CMS类型，选择合适的POC验证漏洞 V1.0
'''
usage = '''
opt:
    ---------------------------------------------------
    help              帮助
    show              显示参数设置
    set url           目标url                set url http://example.com/
    set type          设置CMS类型，设置后可
                      跳过CMS识别            set type example
    list              显示支持的CMS
    search            搜索POC                search example
    run               执行
    exit              退出
    ---------------------------------------------------
'''

cms_mode = Cms_Model()
mode = poc_db.poc_db()


def get_help():
    print(usage)


def show():
    print(f"[+]url: {cms_mode.url}")
    print(f"[+]type: {cms_mode.type}")


def url_check(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        result = requests.get(url, headers=headers, timeout=20, verify=False)
        if result.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def run():
    if cms_mode.url == "":
        print("[+]请输入有效url")
        return
    if not cms_mode.type:
        cms_scanner = CmsScanner(cms_mode)
        print("[+]执行中...")
        cms_scanner.run()
        if not cms_mode.type:
            print("[+]无法判断CMS类型")
            return
        else:
            print(f"[+]CMS类型为{cms_mode.name}")
    poc = control_poc.control(mode, cms_mode)
    poc.auto_poc()


def cms_list():
    for t in Cms_Enum:
        print(f"[+]支持的CMS类型: {t.value}")


def search(cms):
    poc = control_poc.control(mode, cms_mode)
    poc.search(cms)


def set_url(url):
    global cms_mode
    cms_mode = Cms_Model()
    if url_check(url):
        cms_mode.url = url
    else:
        print("[+]url地址错误")


def set_type(cms_type):
    flag = True
    for t in Cms_Enum:
        if t.value == cms_type:
            cms_mode.type = t
            flag = False
            break
    if flag:
        print("[+]cms类型不支持")


def control(text):
    keys = text.split(" ")
    if len(keys) > 1:
        if keys[0] == "search":
            search(keys[1])
        elif keys[0] == "set":
            if keys[1] == "url":
                set_url(keys[2])
            elif keys[1] == "type":
                set_type(keys[2])
    else:
        if text == "exit":
            exit()
        elif text == "help":
            get_help()
        elif text == "list":
            cms_list()
        elif text == "show":
            show()
        elif text == "run":
            run()


if __name__ == "__main__":
    print(logo)
    get_help()
    while True:
        text = input("->")
        control(text)
