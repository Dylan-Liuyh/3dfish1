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

def test_goldpig():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnActivity").click()
    if poco('activity').offspring('toggleActivity').exists():
        poco('activity').offspring('toggleActivity').click()
        i=5
        while True:
            if poco(text="金猪降福").attr('pos')[1]>0.9:
                poco('activity').offspring('Content').child(type='Toggle')[i].swipe([0,-0.5])
                i=i+4
            else:
                break
    poco(text="金猪降福").click()
    poco("btnRule").click()
    poco('rules').offspring('btnClose').click()
    #for num in range(0,len(poco('Content').child(name='item(Clone) '))):
    exists(Template(r"tpl1658886980698.png", record_pos=(-0.093, -0.097), resolution=(2400, 1080)))
    print("存在300，3000，8000倍渔场显示")
'''新号进不去300倍的渔场
    poco("btn800").click()
    poco("btnShowMenu").click()
    poco("btnLeave").click()
    poco("btnOK").click()
'''


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_goldpig()
    except AssertionError as msg:
        raise msg
