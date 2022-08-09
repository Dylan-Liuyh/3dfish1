# -*- encoding=utf8 -*-
__author__ = "Dylan"
import sys
import os
import codecs
import traceback
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

sys.path.append(os.path.abspath(__file__))
root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("/")[:-3])
sys.path.append(root_path)
from common.common_func import *


def test_saijiremai():
    poco("btnRecharge").click()
    poco("lobbyIcon").click()
    poco("panel0").offspring("btnDetail").click()
    if poco('coin_ratio_detail').offspring('btnClose').exists():
        poco("coin_ratio_detail").offspring("btnClose").click()
    poco("panel0").offspring("btnBuy").click()
    print("拉起980点券支付")
    poco("btnCancel").click()
    poco("panel1").offspring("btnDetail").click()
    if poco('coin_ratio_detail').offspring('btnClose').exists():
        poco("coin_ratio_detail").offspring("btnClose").click()
    poco("panel1").offspring("btnBuy").click()
    print("拉起1980点券支付")
    poco("btnCancel").click()
    poco("panel2").offspring("btnDetail").click()
    if poco('coin_ratio_detail').offspring('btnClose').exists():
        poco("coin_ratio_detail").offspring("btnClose").click()
    poco("panel2").offspring("btnBuy").click()
    print("拉起3280点券支付")
    poco("btnCancel").click()
    poco("leftArrow").click()
    poco("leftArrow").click()
    poco("leftArrow").click()
    poco("btnClose").click()


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_saijiremai()
    except AssertionError as msg:
        raise msg
