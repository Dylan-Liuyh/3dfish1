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

def shouchong_huawei():
    login_huawei()
    shouchong()
    wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
    sleep(2)
    touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
    sleep(2)
    touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
    wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
    touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
    if exists(Template(r"tpl1656986957164.png", record_pos=(0.31, -0.13), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986957164.png", record_pos=(0.31, -0.13), resolution=(2700, 1228)))
    if exists(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228)))
    
    #大厅检测
  
    
      
    
if __name__=='__main__':
    shouchong_huawei()