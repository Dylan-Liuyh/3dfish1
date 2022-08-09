# -*- encoding=utf8 -*-
__author__ = "lucia"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

auto_setup(__file__)



from poco.drivers.unity3d import UnityPoco

import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common.common_func import *



def test_shouchong():
    #click_icon('rightDockScroll','groupChargeBox')
    #点击充值豪礼
    poco('groupChargeBox').child('btnCharge').click()
    #点击充点小钱
    poco('group_content').offspring('btnCharge').click()
    poco('charge').wait_for_appearance()
    poco("anchor").child('Button').click()
    if poco('message_box').exists():
        poco('message_box').offspring('btnOK').click()
        payment()
        poco('PayFailed').wait_for_appearance()
        poco('PayFailed').offspring('btnOK').click()
        poco('close').click()
        if poco('newer_shop').exists():
            poco('close').click()
    #init_icon('rightDockScroll')
                    

               
              

if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_shouchong()
    except AssertionError as msg:
        raise msg

