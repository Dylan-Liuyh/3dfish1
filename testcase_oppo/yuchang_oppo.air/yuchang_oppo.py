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



def yuchang_oppo():
    login_oppo()
    yuchang()
    touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))
    sleep(5)
    if exists(Template(r"tpl1657521740953.png", record_pos=(0.089, -0.106), resolution=(2400, 1080))):
        touch(Template(r"tpl1657521749627.png", record_pos=(-0.317, -0.169), resolution=(2400, 1080)))
        sleep(2)
        '''touch(Template(r"tpl1657521767696.png", record_pos=(-0.116, 0.025), resolution=(2400, 1080)))
        sleep(5)'''
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
    if exists(Template(r"tpl1657003690951.png", record_pos=(0.284, -0.13), resolution=(2700, 1228))):
        touch(Template(r"tpl1657003690951.png", record_pos=(0.284, -0.13), resolution=(2700, 1228)))
        sleep(2)
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
    if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
        touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
        sleep(2)
        
        touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))     
      



    
if __name__=='__main__':
    yuchang_oppo()            