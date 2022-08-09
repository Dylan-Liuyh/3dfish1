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
from common.common_func import *
def test_seasonbp():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco("btnSeasonLobby").click()
    if poco('ui_popup').offspring('season_new').exists():
            poco('ui_popup').offspring('anchor').offspring('btnOK').click()
            print('新赛季开启')
    poco(text="成长").click()
    for num in range(0,len(poco('Content').child(name='icon'))):
        cannon=poco('Content').child(name='icon')[num]
        pos=cannon.attr('pos')
        cannon.click()
    poco(text="兑换").click()
    poco(text="奖励").click()
    poco(text="挑战").click()
    poco(texture="season_help").click()
    poco("season").click()
    poco("week").click()
    poco("task").offspring("icon").click()
    poco("btnGetAll").click()
    try:
        poco(text="确 定").click()
        poco(text="关 闭").click()
    except:
        poco("btnOK").click()
    poco("btnClose").click()
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_seasonbp()
    except AssertionError as msg:
        raise msg
        
        
