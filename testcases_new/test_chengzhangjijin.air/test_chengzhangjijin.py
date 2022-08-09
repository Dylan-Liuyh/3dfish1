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

#使用点券解锁
def test_unlock():
    #未解锁
    if poco('activity').offspring('btnBuy').exists():
        poco('activity').offspring('btnBuy').click()
        poco('buy').wait_for_appearance()
        poco('buy').offspring('btnBuy').click()
        #解锁
        if poco('message_box').exists():
            #点券不足，拉起支付后放弃支付
            if '点券不足' in poco('message_box').offspring('tips').get_text():
                poco('message_box').offspring('btnOK').click()
                payment()
                poco('PayFailed').offspring('btnOK').click()
            #点券充足，直接兑换
            else:
                poco('message_box').offspring('btnOK').click()
                poco('message_box').offspring('btnOK').click()
            poco('buy').offspring('btnClose').click()
       
                
                
#一键领奖
def test_getall():
    if poco('btnGetAll').exists():
        poco('btnGetAll').click()
        #没有奖励可以领取
        if poco('message_box').exists():
            poco('message_box').offspring('btnOK').click()
        else:
            sleep(4)
    

def test_chengzhangjijin():
    #成长基金存在
    if poco('btnActivity').exists():
        poco('btnActivity').click()
        #点击活动
        if activity_click('toggleActivity','成长基金')==1:
            test_getall()
            test_unlock()
        poco('activity').offspring('btnClose').click()
            
        
    else:
        print('大厅不存在成长基金功能')
    
    

    
    
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_chengzhangjijin()
    except AssertionError as msg:
        raise msg
