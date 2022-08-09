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
def test_friendinvite():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnActivity").click()
    if poco('activity').offspring('toggleActivity').exists():
        poco('activity').offspring('toggleActivity').click()
        i=5
        while True:
            if poco(text="好友邀请").attr('pos')[1]>0.9:
                poco('activity').offspring('Content').child(type='Toggle')[i].swipe([0,-0.5])
                i=i+4
            else:
                break
    poco(text="好友邀请").click()
    poco("btnGet").click()

    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    if poco(text="登录微信").exists():
        touch(Template(r"tpl1659002645786.png", target_pos=4, record_pos=(-0.007, -0.944), resolution=(1080, 2400)))
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    if poco("activity").offspring("btnClose").exists():
        print("已跳转至活动界面")
    sleep(3.0)

if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        #poco.use_render_resolution()
        test_friendinvite()

    except AssertionError as msg:
        raise msg
