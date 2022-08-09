# -*- encoding=utf8 -*-
__author__ = "Hyper"
import sys
import codecs
import traceback

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common_airtest.common_airtest_all import *

def daozhang_huawei():
    login_huawei()
    daozhang()
    zhifubao_huawei()
    if exists(Template(r"tpl1656931284320.png", threshold=0.8500000000000001, record_pos=(0.018, 0.042), resolution=(2700, 1228))):
        touch(Template(r"tpl1656931284320.png", threshold=0.8500000000000001, record_pos=(0.018, 0.042), resolution=(2700, 1228)))
        
    sleep(2)  
    if exists(Template(r"tpl1656931309155.png", record_pos=(0.286, -0.13), resolution=(2700, 1228))):
        touch(Template(r"tpl1656931309155.png", record_pos=(0.286, -0.13), resolution=(2700, 1228)))
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
        
if __name__=='__main__':
    daozhang_huawei()
        