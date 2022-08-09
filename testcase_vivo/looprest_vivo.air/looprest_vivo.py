# -*- encoding=utf8 -*-
__author__ = "apple"
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

def looprest_vivo():
    login_vivo()
    looprest()
    touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659511988577.png", record_pos=(0.043, 0.07), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659512015562.png", record_pos=(0.158, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659512042281.png", record_pos=(0.155, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    swipe(Template(r"tpl1656986814966.png", record_pos=(0.177, -0.002), resolution=(2700, 1228)), vector=[-0.4977, 0.0258])
    touch(Template(r"tpl1659512068508.png", record_pos=(-0.117, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659512084946.png", record_pos=(-0.004, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659512097565.png", record_pos=(0.107, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    touch(Template(r"tpl1659512114991.png", record_pos=(0.225, 0.072), resolution=(2400, 1080)))
    sleep(2)
    start_app("com.tuyoo.fish3d.vivo")
    if exists(Template(r"tpl1656986957164.png", record_pos=(0.31, -0.13), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986957164.png", record_pos=(0.31, -0.13), resolution=(2700, 1228)))
    if exists(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228)))


   
           
    
if __name__=='__main__':
    looprest_vivo()