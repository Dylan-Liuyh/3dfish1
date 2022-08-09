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

#遍历捕鱼成就，领取奖励
def travers_rewards():
    for list_item in poco('sub_detail').offspring(type='Button'):
        list_item.click()
        #节点不刷新，只能领取第一个
        for reward in poco('GameObject').child('Scroll View').child('Viewport').child('Content').child(type='Node'):
                if reward.child('Button').attr('clickable')==True:
                    reward.child('Button').click()
                else:
                    break  

        


def test_achievement_shengya():
    #成就存在
    if poco(texture="lobby_btn_aachievement").exists():
        poco(texture="lobby_btn_aachievement").click()
        poco('achievement_main').wait_for_appearance()
       
        #点击捕鱼成就
        pos=poco(text='捕鱼成就').attr('pos')
        if pos[1]>0.9:
            print('超出屏幕')
            poco('item_cell').click()
            poco(text='捕鱼成就').click()
        poco(text='捕鱼成就').click()
        travers_rewards()
        
        poco('achievement_main').offspring('Button').click()
        
        
            
        
    else:
        print('大厅无成就按钮')

if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_achievement_shengya()
    except AssertionError as msg:
        raise msg
