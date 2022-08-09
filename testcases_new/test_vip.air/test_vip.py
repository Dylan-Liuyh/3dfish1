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




#遍历点击vip特权
def travers_click_vip():
    #遍历特权等级
    for item in poco('ui_popup').offspring('vip').offspring('vip_cell'):
        pos=item.attr('pos')
        #特权等级超出特权弹窗，向左滑动
        if pos[0]>0.7:
            item.swipe([-0.2,0])
        #点击展示特权详细信息
        item.click()
        #退出特权详细信息，返回特权弹窗
        poco('ui_popup').offspring('vipDetail').offspring('Button').click()
        
        
        
#拉起充值
def pull_up_to_pay():
    #充值按钮存在，点击拉起支付
    if poco('ui_popup').offspring('vip').offspring('btnCharge').exists():
        poco('ui_popup').offspring('vip').offspring('btnCharge').click()
        #关闭首充礼包
        if poco('ui_popup').offspring('charge').exists():
            poco('ui_popup').offspring('charge').offspring('close').click()
        #关闭商城
        if poco('ui_popup').offspring('newer_shop').exists():
            poco('ui_popup').offspring('newer_shop').offspring('close').click()
            

#点击个人信息旁特权，进入特权页面
def navigation_bar_entry():
    #顶部导航栏存在入口
    if poco('UI').offspring('iconVip').exists():
        #点击进入
        poco('UI').offspring('iconVip').click()
        poco('ui_popup').offspring('vip').wait_for_appearance()
        #关闭
        poco('ui_popup').offspring('vip').offspring('btnClose').click()

        
def test_vip():
    click_icon('leftDockScroll','vip_btn')
    poco('ui_popup').offspring('vip').wait_for_appearance()
    travers_click_vip()
    pull_up_to_pay()
    navigation_bar_entry()
    init_icon('leftDockScroll')
    
    



if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_vip()
    except AssertionError as msg:
        raise msg


