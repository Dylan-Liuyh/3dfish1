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


def test_3daysgift():
    click_icon('leftDockScroll',"3day_gift_btn")
    if exists(Template(r"tpl1657782697127.png", record_pos=(0.062, 0.019), resolution=(2400, 1080))):
        if poco('3day_gift').offspring('btnGetReward').exists():
            poco('3day_gift').offspring('btnGetReward').click()
            poco(text="领取奖励").click()
            if poco('3day_gift').offspring('reward_5').exists():
                print("领取奖励成功")
        else:
            if poco('3day_gift').offspring('btnNextDay').exists():
                print("奖励已被领取，明天再来")

        poco("btnClose").click()


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_3daysgift()
    except AssertionError as msg:
        raise msg