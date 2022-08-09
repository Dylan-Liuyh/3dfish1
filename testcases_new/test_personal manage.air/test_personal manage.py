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

def test_personal():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("head").click()
    poco("name").click()
    poco("btnConfirm").click()
    poco("btnOK").click()
    poco("btnCancel").click()
    poco("label").click()
    poco("user_info").child("anchor").offspring("btnClose").click()
    if poco(text="账号升级").exists():
        poco(text="账号升级").click()
        exists(Template(r"tpl1657175623568.png", record_pos=(0.018, -0.121), resolution=(1600, 720)))
        poco(texture="certification_btn_close").click()
    else:
        poco("btnClose").click()
    
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        test_personal()
    except AssertionError as msg:
        raise msg
