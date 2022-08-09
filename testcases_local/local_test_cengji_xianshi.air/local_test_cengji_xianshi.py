# -*- encoding=utf8 -*-
__author__ = "Dylan"
import sys
import os
import codecs
import traceback
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from airtest.report.report import LogToHtml

from airtest.core.android.recorder import *
from airtest.core.android.adb import *
sys.path.append(os.path.abspath(__file__))
root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("/")[:-3])
sys.path.append(root_path)
ST.FIND_TIMEOUT=300
#from common.common_func import *

def test_start():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnQuickStart").click()
    poco("btnShowMenu").click()
    poco("btnChangeWeapon").click()
    
def travers_cannon_attribute():
    #获取按钮
    poco('tabs').child('cannon').click()
    if poco('btnEquip').exists():
        poco('btnEquip').click()
        if poco('pop_get_material').offspring('btnClose').exists():
            poco('pop_get_material').offspring('btnClose').click()
    #炮台效果
    if poco('detail').offspring('Content').child().exists():
        for item in poco('detail').offspring('Content').child():
            item.click()
    #炮台特性
    if poco('speciality').offspring('Content').child().exists():
        for item in poco('speciality').offspring('Content').child():
            item.click()
    #炮台星级
    if poco('level').offspring('btnAdd').exists():
        poco('level').offspring('btnAdd').click()
        poco("anchor").offspring("btnClose").click()
        
        
def travers_cannon():
    
    #选择炮台

    poco('tabs').child('cannon').click()
    
    #遍历已解锁炮台
    for num in range(0,len(poco('unlocked').child(name='item_cannon'))):
        cannon=poco('unlocked').child(name='item_cannon')[num]
        pos=cannon.attr('pos')
        if pos[1]>0.6:
            cannon.swipe([0,-0.2])
        cannon.click()
        poco("btnEquip").click()
        poco("btnClose").click()
        poco("btnFishBook").click()
        poco("boss_huangjinlinhuo").click()
        poco("btnClose").click()
        poco("btnSetting").click()
        poco("btnClose").click() 
        poco("skill_lock").click()
        sleep(5.0)
        test_qiangzhitanchuang()
        wait(Template(r"tpl1657873658834.png", record_pos=(0.019, 0.148), resolution=(2400, 1080)))
        #exists(Template(r"tpl1657873658834.png", record_pos=(0.019, 0.148), resolution=(2400, 1080)),timeout=ST.FIND_TIMEOUT)
        print("炮台层级无问题")
        poco("btnChangeWeapon").click()
        sleep(5.0)
        test_qiangzhitanchuang()
        sleep(10.0)
        travers_cannon_attribute()

def test_qiangzhitanchuang():
    if poco("rank_3").offspring("btnClose").exists():
        poco("rank_3").offspring("btnClose").click()
    if poco("level_up").offspring("btnGet").exists():
        poco("level_up").offspring("btnGet").click()
    

if __name__=='__main__':
    try:
        #common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_start()
        travers_cannon_attribute()
        test_qiangzhitanchuang()
        travers_cannon()
    except AssertionError as msg:
        raise msg



