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

def test_quick_start():
    poco("btnQuickStart").click()
    if poco("RootUI").exists:
        print("成功进入渔场")
        sleep(10)
        poco('btnShowMenu').click()
        poco('btnLeave').click()
        poco('ui_popup').offspring('btnOK').click()
    else:
        print("报错！！点击快速开始无反应")



if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_quick_start()
    except AssertionError as msg:
        raise msg