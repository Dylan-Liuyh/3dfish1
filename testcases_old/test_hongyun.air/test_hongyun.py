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
#poco(texture="lobby_btn_lucky").click()
#poco("btnRank").click()
def test_hongyun():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    click_icon('leftDockScroll',"btn")
    poco("btnRank").click()
    if poco('rank_new').offspring('btnPreview').exists():
        poco('rank_new').offspring('btnPreview').click()
        poco("btnClose").click()
    poco("btnRule").click()
    if poco('anchor').offspring('title').exists():
        poco('rule').offspring('btnClose').click()
        print("活动规则存在")
    poco("btnDraw1").click()
    poco('shop').offspring('btnClose').click()
    poco("btnDraw5").click()
    poco('shop').offspring('btnClose').click()
    poco("skip").click()
    poco("btnClose").click()
    init_icon('leftDockScroll')
    '''for num in poco('items').offspring('item').child(name='icon'):
        wen=poco('items').child("name=icon")[num]
        pos=wen.attr('pos')
        if pos[1]>0.7:
            wen.swipe([0,-0.2])
        wen.click()
        if num>3:
            break'''


if __name__=='__main__':
    try:
        test_hongyun()
        #旧版
    except AssertionError as msg:
        raise msg
