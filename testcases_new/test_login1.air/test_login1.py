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


def test_login():
    #游戏内点击返回，重新登录
    if poco('btnBack').exists():
        poco('btnBack').click()
        poco('message_box').offspring('btnOK').click()
        poco('loginNew').wait_for_appearance(timeout=120)
        #手机号、密码
        account='18811792508'
        password='Tuyoo123'
        
        #点击切换账号
        poco('user').child('logout').click()
        poco('accountPanel').wait_for_appearance()
        poco('password').child('mobile').click()
        text(account)
        poco('password').child('passwd').click()
        poco('password').child('passwd').click()
        text(password)
        poco('password').child('passwd').click()
        poco('loginBtn').click()
        poco('btnPlay').click()
        #输入法切换导致账号未输入成功
        if poco('message_box').exists():
            poco('message_box').offspring('btnOK').click()
            poco('password').child('mobile').click()
            text(account)
            poco('password').child('passwd').click()
            poco('loginBtn').click()
            poco('btnPlay').click()
        common_close_popups_one_by_one_if_need()
        


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_login()
    except AssertionError as msg:
        raise msg