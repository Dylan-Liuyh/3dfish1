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
ST.FIND_TIMEOUT=20
from common.common_func import *
from airtest.core.api import *


def test_chaoshikong():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnMagicBox").click()
    poco("toggleArtifact").click()
    for num in range(0,len(poco('artifact').child('items').offspring('icon'))):
        box=poco('artifact').child('items').offspring('icon')[num]
        pos=box.attr('pos')
        box.click()
    poco("btnGet").click()
    if poco('reward_title_1').exists():
        print('领奖成功')
    sleep(3.0)
    if poco(text='去充值').exists():
        poco(text='去充值').click()
        if poco('btnDailyGift').exists():
            print('已跳转至商城')
    elif poco(text='抽奖').exists():
        poco(text='抽奖').click()
        if poco('reward_title_1').exists():
            sleep(3.0)
            print('领奖成功')
        else:
            assert_not_exists(Template(r"tpl1658736421910.png", record_pos=(-0.022, -0.133), resolution=(2400, 1080)), "今日已经领取过啦")
    poco("toggleMecha").click()
    for num in range(0,len(poco('mecha').child('items').offspring('icon'))):
        box=poco('mecha').child('items').offspring('icon')[num]
        pos=box.attr('pos')
        box.click()
    if poco('btnBox').exists():
        poco('btnBox').click()
        exists(Template(r"tpl1658736421910.png", record_pos=(-0.022, -0.133), resolution=(2400, 1080)))
        print("奖励领取成功")        
    else:
        sleep(3.0)
        print('奖励以领取过')
    poco("btnBox").click()
    poco("btnGet").click()
    if poco('reward_title_1').exists():
        print('领奖成功')
    sleep(3.0)
    if poco(text='去充值').exists():
        poco(text='去充值').click()
        if poco('btnDailyGift').exists():
            print('已跳转至商城')
    elif poco(text='抽奖').exists():
        poco(text='抽奖').click()
        if poco('reward_title_1').exists():
            sleep(3.0)
            print('领奖成功')
        else:
            assert_not_exists(Template(r"tpl1658736421910.png", record_pos=(-0.022, -0.133), resolution=(2400, 1080)), "今日已经领取过啦")

    sleep(3.0)
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_chaoshikong()
    except AssertionError as msg:
        raise msg
