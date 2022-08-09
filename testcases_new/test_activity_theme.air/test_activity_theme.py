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
from poco.drivers.unity3d import UnityPoco
def test_activity_theme():
    poco = UnityPoco()
    poco.use_render_resolution()
    poco('btnActivity').click()
    if poco(name='theme_bg').exists():
        poco(name='theme_bg').click()
        print('theme exists')
    else:
        print('theme not exsists!!!error!!!')
    poco('activity').offspring('btnClose').click()
    poco('btnTheme').click()
    if poco(name='theme_bg').exists():
        poco(name='theme_bg').click()
        print('theme exists')
    else:
        print('theme not exsists!!!error!!!')
    poco('activity').offspring('btnClose').click()
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_activity_theme()
    except AssertionError as msg:
        raise msg