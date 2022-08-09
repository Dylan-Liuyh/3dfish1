# -*- encoding=utf8 -*-
__author__ = "Lucia"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common.common_func import *



#预计点券数额
def test_total(init_num,add_num):
    return init_num+add_num

#购买点券、支付到账校验
def test_check():
    #初始金币
    init_coupon=int(poco('lobbyTop').child('labConch').attr('text').replace(',',''))
    
    #购买点券
    poco('lobbyTop').child('btnConch').click()
    #关闭首充礼包
    if poco('ui_popup').offspring('charge').exists():
        poco('ui_popup').offspring('charge').offspring('close').click()
    if poco('newer_shop').exists():
        poco('btnCoupon').click()
        poco(text="￥1").click()
        payment_zfb()
        poco('message_box').offspring('btnOK').click()
        poco('newer_shop').offspring('close').click()
        common_close_popups_one_by_one_if_need()
        total_coupon=test_total(init_coupon,12)
        now_coupon=int(poco('lobbyTop').child('labConch').attr('text').replace(',',''))
        assert_equal(total_coupon,now_coupon)
        
        
        
        
        
        
        
        
        
"""def test_icon_accounting():
    icon_num=poco('lobbyTop').child('labGold').attr('text')
    if icon_num.endswith('万') or icon_num.endswith('亿') or icon_num.endswith('兆'):
        print('暂不处理,后续再优化')
    else:
        test_check()"""
            
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_check()
    except AssertionError as msg:
        raise msg