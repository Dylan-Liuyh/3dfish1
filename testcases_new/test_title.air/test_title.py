# -*- encoding=utf8 -*-
__author__ = "Dylan"
import sys
import os
import codecs
import traceback
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

sys.path.append(os.path.abspath(__file__))
root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("/")[:-3])
sys.path.append(root_path)
from common.common_func import *

def test_title():

    poco("btnActivity").click()
    if poco('activity').offspring('toggleNotice').exists():
        poco('activity').offspring('toggleNotice').click()
        #反作弊公告超出活动栏
        i=5
        while True:
            if poco(text="反作弊公告").attr('pos')[1]>0.9:
                poco('activity').offspring('Content').child(type='Toggle')[i].swipe([0,-0.5])
                i=i+4
            else:
                break
    if poco(text="反作弊公告").exists():
        poco(text="反作弊公告").click()
        poco('activity_text').attr("亲爱的玩家您好：为了维护公平公正的游戏环境，保障广大玩家的正常利益，《捕鱼大作战3D》将通过封禁帐号等措施严厉打击非正常游戏行为。非正常游戏行为包括但不限于：1. 利用游戏漏洞盗刷金币、点券、道具等，谋取游戏利益，破坏游戏公平秩序2. 安装使用影响游戏平衡的第三方软件3. 同一个玩家（或同一IP）同时登录多个账号角色4. 在游戏内直接或者变相倒卖游戏金币、游戏道具、游戏账号等5. 在游戏内宣扬色情暴力信息、欺诈性无关广告等处罚力度包括但不限于：1. 取消玩家因不正常游戏行为获得的奖励（包括但不限于游戏金币、道具、点券）1. 根据情节严重程度，对相关账号做出暂时或永久封禁、删除账号及数据等处罚措施1. 情节严重、造成重大影响的非正常游戏行为，官方将会移交有关机构处理，并且追究法律责任希望广大玩家能够保护好自己的账号安全和个人隐私，公平游戏、健康游戏。同时希望大家与我们一起为绿色健康的环境努力，若发现非正常游戏行为，点击客服进行举报。")
        print('捕鱼大作战3D反作弊公告存在')
        poco(text="反赌博公告").click()
        poco('activity_text').attr("亲爱的玩家您好：为了维护纯净的游戏环境，保障广大玩家的正常利益，《捕鱼大作战3D》将严惩游戏内外与“赌博”相关的行为。玩家不得在游戏内外通过任何方式传播赌博信息、进行各种性质的赌博活动。一经核实或有合理理由认为玩家存在上述行为，官方将视情节严重程度，做出暂时或者永久封禁相关账号的处罚！影响特别恶劣者，官方将移交有关机构处理。玩家若发现上述与“赌博”相关的行为，可以点击登录界面或者大厅顶部的客服按钮进入举报。 ")
        print("捕鱼大作战3D反赌博公告存在")
        poco(text="健康游戏公告").click()
        poco('activity_text').attr("抵制不良游戏，拒绝盗版游戏。注意自我保护，谨防上当受骗。适度游戏益脑，沉迷游戏伤身。合理安排时间，享受健康生活。亲爱的玩家您好：《捕鱼大作战3D》一直以来都期待与玩家携手，共同维护健康和谐的游戏环境。在此，我们郑重声明：1. 游戏内金币为游戏道具，不具有实际货币属性和货币价值，官方不会提供任何形式的回购、直接或者变相地兑换现金和实物、转让、转赠的功能，同时禁止玩家之间金币交易、金币转让、金币赠予的行为。2. 玩家注册的游戏账号仅限本人使用不得交易，禁止以任何形式赠予、借用、出租、转让、售卖或以其他任何方式许可他人使用该账号。同时官方从未授权任何第三方/平台出租、转让或售卖游戏账号。3. 坚决抵制不健康及赌博等违法违规行为（包括宣扬色情暴力信息、欺诈性无关广告等），以及违背游戏公平的作弊行为。4. 请玩家保护好个人隐私，请勿在游戏内暴露真实个人信息，请勿相信游戏内聊天频道出现的代充、折扣广告。5. 官方不会向玩家索取财物和账号的密码信息，核实问题只需要玩家提供游戏ID账号、游戏截图、微信号等。请玩家切勿将账号密码共享他人，因账号共享导致的损失由玩家自行承担。如官方发现或有合理理由认为玩家存在上述违规行为，官方有权立即暂停或终止提供服务，暂时或永久禁用相关账号并依法追究其它责任。若玩家发现任何游戏违规行为，可以点击登录界面或大厅顶部的客服按钮进行举报，感谢您的理解与支持！ ")
        print("捕鱼大作战3D健康游戏公告存在")
        poco(text="防沉迷公告").click()
        poco('activity_text').attr('text="亲爱的玩家您好：根据国家新闻出版署发布的《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》，《捕鱼大作战3D》积极落实通知要求，已上线未成年防沉迷系统，未成年人账号不能登录游戏游玩、进行游戏充值。《捕鱼大作战3D》严格遵守制度守护未成年人的成长环境、保护未成年人身心健康。《捕鱼大作战3D》一直致力于为玩家带来健康快乐的游戏体验，为了您的健康生活，请您合理安排游戏时间，在享受快乐的同时适度休息。"')
        print("防沉迷公告存在")

    
if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_title()
    except AssertionError as msg:
        raise msg