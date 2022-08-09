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
def test_everyday_mission():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnActivity").click()
    i=5
    while True:
        if poco(text="每日任务").attr('pos')[1]>0.9:
            poco('activity').offspring('Content').child(type='Toggle')[i].swipe([0,-0.5])
            i=i+4
        else:
            break
    if poco(text="每日任务").exists():
            poco(text="每日任务").click()

    #遍历活跃度礼包按钮
    for num in range(0,len(poco('prize').child('box'))):
        box=poco('prize').child(name='box')[num]
        pos=box.attr('pos')
        box.click()
    '''
    暂取消swipe遍历
    i=5
    while True:
        if poco(text="累计使用道具5次(1/5)").attr('pos')[1]>0.9:
            poco('activity').offspring('item(Clone)').child('icon')[i].swipe([0,-0.2])
            i=i+4
        else:
            break
            '''
    poco(text="点击此处邀请好友！(0/1)").click()
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    if poco(text="登录微信").exists():
        print("成功跳转至微信")
        touch(Template(r"tpl1659002865813.png", target_pos=4, record_pos=(-0.003, -0.942), resolution=(1080, 2400)))
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("btnClose").click()


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_everyday_mission()
    except AssertionError as msg:
        raise msg