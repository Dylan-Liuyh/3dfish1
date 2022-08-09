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

def guizuyueka_vivo():
    login_vivo()
    guizuyueka()
    if exists(Template(r"tpl1659680508065.png", record_pos=(-0.099, 0.152), resolution=(2700, 1228))):        #300
        touch(Template(r"tpl1659680508065.png", record_pos=(-0.099, 0.152), resolution=(2700, 1228)))
        while True:
            if exists(Template(r"tpl1659671744136.png", record_pos=(0.019, -0.034), resolution=(2700, 1228))):
                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))    
                sleep(5)
            elif exists(Template(r"tpl1659672170495.png", record_pos=(0.023, -0.033), resolution=(2700, 1228))):

                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))
                sleep(5)
                start_app("com.tuyoo.fish3d.vivo")
                break
    elif exists(Template(r"tpl1659671979419.png", record_pos=(-0.011, 0.151), resolution=(2700, 1228))):
        touch(Template(r"tpl1659671979419.png", record_pos=(-0.011, 0.151), resolution=(2700, 1228)))
        while True:
            if exists(Template(r"tpl1659671744136.png", record_pos=(0.019, -0.034), resolution=(2700, 1228))):
                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))    
                sleep(5)
            elif exists(Template(r"tpl1659672170495.png", record_pos=(0.023, -0.033), resolution=(2700, 1228))):

                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))
                sleep(5)
                start_app("com.tuyoo.fish3d.vivo")
                break
        
        
    if exists(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080))):        
        touch(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080)))
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
        
        

if __name__=='__main__':
    guizuyueka_vivo()           