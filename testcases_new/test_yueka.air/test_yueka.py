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

#遍历贵族月卡、至尊月卡 node_item月卡节点名
def travers_yueka(node_item):
    poco('month_card').offspring(node_item).offspring('btn').click()
    if poco('message_box').exists():
        poco('message_box').offspring('btnOK').click()
        payment()
        if poco('PayFailed').exists():
            poco('PayFailed').offspring('btnOK').click()
    
    



def test_yueka():
    #点击充点小钱，打开贵族月卡
    """if poco('btnRecharge').exists():
        poco('btnRecharge').click()
        if poco('btnRecharge').offspring('btnMonthly').exists():
            poco('btnRecharge').offspring('btnMonthly').click()"""
    #点击充值豪礼
    poco('groupChargeBox').child('btnCharge').click()
    #点击贵族月卡
    poco('group_content').offspring('btnMonthCard').click()
    poco('month_card').wait_for_appearance()
    #奖励全揽
    if poco('month_card').offspring('Text',text='奖励全览').exists():
        poco('month_card').offspring('Text',text='奖励全览').click()
        poco('month_card').offspring('Text',text='返回').click()
        travers_yueka('month_card_item1')
        travers_yueka('month_card_item2')
    poco('month_card').offspring('close').click()
                
            
                
            



if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_yueka()
    except AssertionError as msg:
        raise msg