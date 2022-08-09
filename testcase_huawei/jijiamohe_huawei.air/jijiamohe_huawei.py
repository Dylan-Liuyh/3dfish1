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


def jijiamohe_huawei():
    login_huawei()
    jijiamohe()
    '''if exists(Template(r"tpl1657003623825.png", record_pos=(-0.404, -0.066), resolution=(2700, 1228))):
        if exists(Template(r"tpl1657003633692.png", record_pos=(0.018, 0.154), resolution=(2700, 1228))):     
            touch(Template(r"tpl1657003633692.png", record_pos=(0.018, 0.154), resolution=(2700, 1228)))
            #touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
            touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))
            wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
            
            touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
            sleep(2)
            touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
            wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
            touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
            touch(Template(r"tpl1657098485090.png", record_pos=(0.308, -0.136), resolution=(2700, 1228)))
            
    if exists(Template(r"tpl1659434979802.png", record_pos=(-0.409, -0.149), resolution=(2400, 1080))):
        touch(Template(r"tpl1659434979802.png", record_pos=(-0.409, -0.149), resolution=(2400, 1080)))
        if exists(Template(r"tpl1659435209586.png", record_pos=(0.017, 0.155), resolution=(2400, 1080))):
            touch(Template(r"tpl1659435209586.png", record_pos=(0.017, 0.155), resolution=(2400, 1080)))
            #touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
            touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))
            wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
            
            touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
            sleep(2)
            touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
            wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
            touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
            touch(Template(r"tpl1657098485090.png", record_pos=(0.308, -0.136), resolution=(2700, 1228)))
    if exists(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080))):        
        touch(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080)))
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))'''
    if exists(Template(r"tpl1657003623825.png", record_pos=(-0.404, -0.066), resolution=(2700, 1228))):
        if exists(Template(r"tpl1658817700372.png", threshold=0.8500000000000001, record_pos=(0.003, 0.151), resolution=(2700, 1228))):
            touch(Template(r"tpl1658817700372.png", threshold=0.8500000000000001, record_pos=(0.003, 0.151), resolution=(2700, 1228)))
            sleep(20)

        else:
            touch(Template(r"tpl1657003633692.png", record_pos=(0.018, 0.154), resolution=(2700, 1228)))
            sleep(2)
            touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
            wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
            sleep(2)
            touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
            sleep(2)
            touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
            wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
            touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
            sleep(2)
            touch(Template(r"tpl1657098485090.png", record_pos=(0.308, -0.136), resolution=(2700, 1228)))
    if exists(Template(r"tpl1657003738678.png", record_pos=(-0.402, -0.152), resolution=(2700, 1228))):
        touch(Template(r"tpl1657003738678.png", record_pos=(-0.402, -0.152), resolution=(2700, 1228)))
        sleep(2)
        touch(Template(r"tpl1657003768221.png", record_pos=(0.017, 0.157), resolution=(2700, 1228)))
        sleep(2)
        touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
        wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
        sleep(2)
        touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
        sleep(2)
        touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
        wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
        touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
        sleep(2)
        touch(Template(r"tpl1657098485090.png", record_pos=(0.308, -0.136), resolution=(2700, 1228)))

        sleep(2)
    if exists(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080))):        
        touch(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080)))
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))) 
        
if __name__=='__main__':
    jijiamohe_huawei()