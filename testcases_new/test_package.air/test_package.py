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
def test_package():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    poco.use_render_resolution()
    if poco("btnPack").exists():
        poco("btnPack").click()
        if poco(text='锁定').exists():
            poco("boardLeft").offspring('btnLeft').click()
        poco('btnCancel').click()
    poco("btnClose").click()

    '''
for num in range(0,len(poco('bag').child('anchor').child('boardRight').child('bag_item(Clone)').offspring('btnItem'))):
        box=poco('bag').child('anchor').child('boardRight').child('bag_item(Clone)').offspring('btnItem')[num]
        pos=box.attr('pos')
        box.click()'''

        
   



if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_package()
    except AssertionError as msg:
        raise msg
