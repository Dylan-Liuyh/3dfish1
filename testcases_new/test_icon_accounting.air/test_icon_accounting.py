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

def test_total(init_num,add_num):
    return init_num+add_num


def test_check():
    #初始金币
    init_icon=int(poco('lobbyTop').child('labGold').attr('text').replace(',',''))
    
    #金币到账
    poco('lobbyTop').child('btnGold').click()
    #关闭首充礼包
    if poco('ui_popup').offspring('charge').exists():
        poco('ui_popup').offspring('charge').offspring('close').click()
        if poco('ui_popup').offspring('newer_shop').exists():
            #日礼包
            poco('btnDailyGift').click()
            print(poco('newer_shop_gift').offspring('item').offspring('price').get_text())
            if poco('newer_shop_gift').offspring('item').offspring('price').get_text()=='0点券':
                #金币数额
                add_icon=int(poco('newer_shop_gift').offspring('item').offspring('count').get_text().replace(',',''))
                #领取免费日礼包
                poco('newer_shop_gift').offspring('item').child('bg').click()
                sleep(4)
                poco('newer_shop').offspring('close').click()
                except_num=test_total(init_icon,add_icon)
                total=int(poco('lobbyTop').child('labGold').attr('text').replace(',',''))
                assert_equal(total,except_num)
            else:
                print('免费日礼包已被领取')
                poco('newer_shop').offspring('close').click()
                
def test_icon_accounting():
    icon_num=poco('lobbyTop').child('labGold').attr('text')
    if icon_num.endswith('万') or icon_num.endswith('亿') or icon_num.endswith('兆'):
        print('暂不处理,后续再优化')
    else:
        test_check()
            
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_icon_accounting()
    except AssertionError as msg:
        raise msg