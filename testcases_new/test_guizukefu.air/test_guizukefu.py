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
from common.common_func import *
def test_kefu():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco(texture="lobby_icon_customer").click()

    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    if poco(text="捕鱼大作战").exists():
        poco(text="捕鱼大作战").click()
        print("已跳转到客服界面")
        poco("com.tuyoo.fish3d.official:id/aihelp_iv_back").click()

if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_kefu()
    except AssertionError as msg:
        raise msg
