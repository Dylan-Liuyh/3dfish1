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
def test_kaiyun():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnActivity").click()
    if activity_click('toggleActivity','开运福利')==1:
        if poco("guangzhu03_mask_button_kaiyun").exists():
            poco("guangzhu03_mask_button_kaiyun").click()
        if poco('GameObject').offspring('title_reward').exists():
            sleep(4.0)
            if poco('content').offspring('get_disable').exists():
                sleep(2.0)
                print("奖励不可重复领取")
        if poco('dice').offspring('Button').exists():
            poco('dice').offspring('Button').click()
        if poco('bottom').offspring('panel').exists():
                sleep(10.0)
                print("跳转至幸运骰子")
        if poco('dice').offspring('bottom_board').exists():
                sleep(2.0)
                print("奖励不可重复领取")
        if poco('roulette').offspring('Button').exists():
                poco('roulette').offspring('Button').click()
        if poco('center').offspring('Button').exists():
                poco('center').offspring('Button').click()
                sleep(10.0)
                print("跳转至彩金转轮")
        if poco('roulette').child('counter_image').offspring('bottom_board').exists():
                sleep(2.0)
                print("奖励不可重复领取")
    poco('activity').offspring('btnClose').click()
    




if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        test_kaiyun()
    except AssertionError as msg:
        raise msg