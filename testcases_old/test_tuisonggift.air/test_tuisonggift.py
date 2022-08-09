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
def test_tuisong():
    poco = UnityPoco()
    poco("btnActivity").click()
    i=5
    while True:
        if poco(text="推送礼包").attr('pos')[1]>0.9:
            poco('activity').offspring('Content').child(type='Toggle')[i].swipe([0,-0.5])
            i=i+4
        else:
            break
    if poco(text="推送礼包").exists():
        poco(text="推送礼包").click()
    exists(Template(r"tpl1658485692657.png", threshold=0.7, rgb=False, record_pos=(0.069, -0.033), scale_max=800, resolution=(2400, 1080)))
    poco("GetButton").click()
    if poco("title_reward").exists():
        print("成功领取奖励")
    elif exists(Template(r"tpl1658715781037.png", record_pos=(-0.016, -0.039), resolution=(2400, 1080))):
        print("本周以领取过奖励")
    sleep(3.0)
    poco("btnClose").click()



if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_tuisong()
    except AssertionError as msg:
        raise msg