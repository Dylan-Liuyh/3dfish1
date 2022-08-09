# -*- encoding=utf8 -*-
__author__ = "Dylan"
import sys
import os
import codecs
import traceback
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

sys.path.append(os.path.abspath(__file__))
root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("/")[:-3])
sys.path.append(root_path)
from common.common_func import *

def test_shenshou():
    click_icon('rightDockScroll',"btnMonster")
    if poco('ui_popup').offspring('big_monster_intro').exists():
        print("神兽传说界面存在")
        poco('big_monster_intro').offspring('Button').click()

if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_shenshou()
    except AssertionError as msg:
        raise msg

    
