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




#遍历邮件
def travers_mails():
    while True:
        if poco('ScrollMail').offspring(name='mail_item').exists():
            mail_node=poco('ScrollMail').offspring(name='mail_item')[0]
            mail_node.click()
            #删除邮件
            if poco('btnDelOne').exists():
                poco('btnDelOne').click()
            #领取奖励
            elif poco('btnReceive').exists():
                poco('btnReceive').click()
                #poco('reward_5').wait_for_appearance(timeout=30)
                sleep(4)
                if poco('btnDelOne').exists():
                    poco('btnDelOne').click()
            if len(poco('ScrollMail').offspring(name='mail_item'))<=2:
                break
        else:
            break
    #一键删除
    if poco('btnDel').exists():
        poco('btnDel').click()
    poco("btnClose").click()
    

    
        
            
        

def test_mail():
    if poco('btnMenu').exists():
        poco("btnMenu").click()
        #根据数量来断定邮件位置
        if len(poco('menu').child(type='Button'))==6:
            poco('menu').child('btn_3').click()
        else:
            poco('menu').child('btn_4').click()
        poco('mail').wait_for_appearance(60)
        travers_mails()
        poco("btnMenu").click()
        





if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_mail()
    except AssertionError as msg:
        raise msg
