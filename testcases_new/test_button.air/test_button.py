# -*- encoding=utf8 -*-
__author__ = "Lucia,Dylan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common.common_func import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

def travers_close():
    sleep(5)
    if exists(Template(r"tpl1658907232293.png", record_pos=(-0.437, -0.106), resolution=(2400, 1080))):
        touch(Template(r"tpl1658907251378.png", record_pos=(-0.447, -0.168), resolution=(2400, 1080)))


    poco=UnityPoco()
    poco.use_render_resolution()
    #关闭设置弹窗
    if poco('setting').exists():
        poco('setting').offspring('btnClose').click()
        
    #关闭概率公式
    elif poco('ui_popup').offspring('notice').exists():
        poco('notice').offspring('btnClose').click()
        
    #关闭签到
    elif poco('sign_in').exists():
        poco('sign_in').offspring('btnClose').click()
        sleep(4)
        #可签到，领取奖励后，关闭签到弹窗
        if poco('sign_in').exists():
            poco('sign_in').offspring('btnClose').click()
    #关闭邮件
    elif poco('mail').exists():
        poco('mail').offspring('btnClose').click()
    #关闭兑换商城
    elif poco('huanqu_shop').exists():
        poco('huanqu_shop').offspring('Button').click()
    #关闭兑换码
    elif poco('code_view').exists():
        poco('code_view').offspring('Button (1)').click()

        



#设置按钮遍历
def test_button():
    poco=UnityPoco()
    poco.use_render_resolution()
    if poco('btnMenu').exists():
        poco('btnMenu').click()
        for item in poco('menu').child(type='Button'):
            item.click()
            travers_close()
        poco('btnMenu').click()
            
        
        
        
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        test_button()
    except AssertionError as msg:
        raise msg
