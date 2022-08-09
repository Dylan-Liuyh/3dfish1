# -*- coding=utf-8 -*-
"""
Created by lichen on 2021/3/16.
"""

# 50%概率捕获，SERVERIDS填写:
# 测试服：GT00280011001,GT00280021001,GT00280031001,GT00280041001,GT00280081001,GT00280081002,GT00280081003,GT00280091001,GT00280091002,GT00280141001
# 仿真服：GT00280011001,GT00280011002,GT00280011003,GT00280011004,GT00280011005,GT00280011006,GT00280011007,GT00280011008,GT00280021001,GT00280021002,GT00280021003,GT00280021004,GT00280021005,GT00280021006,GT00280021007,GT00280022001,GT00280022002,GT00280022003,GT00280022004,GT00280022005,GT00280022006,GT00280022007,GT00280031001,GT00280031002,GT00280031003,GT00280031004,GT00280031005,GT00280031006,GT00280031007,GT00280031008,GT00280041001,GT00280041002,GT00280041003,GT00280041004,GT00280041005,GT00280041006,GT00280051001,GT00280061001,GT00280071001,GT00280081001,GT00280081002,GT00280081003,GT00280081004,GT00280081005,GT00280081006,GT00280081007,GT00280081008,GT00280081009,GT00280081010,GT00280081011,GT00280091001,GT00280091002,GT00280091003,GT00280091004,GT00280091005,GT00280091006,GT00280091007,GT00280091008,GT00280091009,GT00280091010,GT00280091011,GT00280091012,GT00280091013,GT00280141001,GT00280141002,GT00280141003,GT00280141004,GT00280141005,GT00280141006
from fish.table.table_base import FishTableBase
def _getCatchProbb(self, player, fishConf, energy, fishType):
    probb = self._calcCatchProbb(player, fishConf, energy, fishType)
    # 以下注释打开即为正常概率
    # return probb
    return 50000
FishTableBase._getCatchProbb = _getCatchProbb
# 50%概率捕获


# 支付测试, SERVERIDS填写:HT9999000001
# TY28_WEEKMEMBER002
# TY28P000610102        # 首充礼包
# TY28_WEEKMEMBER       # 6元周卡
# TY28_WEEKMEMBER003    # 6元->1元周卡
# TY28S000610104        # 6元->1元周卡
# TY28S003010101        # 送激光1的商品
# TY28BKRUPT0008        # 送锁定的商品
# TY28GUF0198001        # 成长基金
# TY28C064810107        # 金币
# TY28D064810207        # 钻石
# TY28DISCOUNT0006      # 迎新特惠
# TY28P000610107        # 财神到6元
# TY28T000601           # 点券6元
# TY28T001201           # 点券12元
# TY28T009801           # 点券98元
# TY28T032801           # 点券328元
# TY28T064801           # 点券648元
# TY28C001210102        # 金币12元
# TY28_MEMBER           # 贵族月卡
# TY28P000610105        # 招财进宝
# TY28BKRPTGIFT03       # 破产礼包
def _main():
    userId = 11543
    productId = "TY28T064801"
    from poker.util import webpage
    from poker.entity.dao import sessiondata
    from poker.entity.configure import gdata
    from hall.entity import hallstore
    serverUrl = gdata.httpSdk()
    product = hallstore.storeSystem.findProduct(productId)
    clientId = sessiondata.getClientId(userId)
    httpUrl = "%s/gtest/store/new_transaction?userId=%d&gameId=9999&clientId=%s&prodId=%s&count=1" % (serverUrl, userId, clientId, productId)
    ret, _ = webpage.webgetJson(httpUrl)
    orderId = ret.get("result", {}).get("orderId", "")
    httpUrl = "%s/gtest/dizhu/store/deliveryOrder?userId=%d&gameId=9999&clientId=%s&prodId=%s&orderId=%s&count=1&chargedRmbs=%s&chargedDiamonds=%s&consumeCoin=%s" % (serverUrl, userId, clientId, productId, orderId, product.price, product.priceDiamond, product.priceDiamond)
    ret, _ = webpage.webget(httpUrl)
from freetime.core.timer import FTLoopTimer
FTLoopTimer(0.1, 0, _main).start()
# 支付测试, SERVERIDS填写:HT9999000001


# 重置充点小钱（首充豪礼）SERVERIDS填写:UT9999000001
def _main():
    userId = 11543
    from poker.entity.dao import gamedata
    fields = [
        "buy.limit.record.TY28P000610102",
        "buy.limit.record.TY28P000510103",
        "buy.limit.record.TY28P000410104",
        "buy.limit.record.TY28S000610104",
        "buy.limit.record.TY28S000510105",
        "buy.limit.record.TY28S000410106",
        "buy.limit.record.TY28P000610103",
        "buy.limit.record.TY28TEXP000610102",
        "buy.limit.record.TY28FRG00060001",
        "buy.limit.record.TY28FRG00300001",
        "buy.limit.record.TY28FRG01980001",
    ]
    gamedata.delGameAttrs(userId, 9999, fields)
from freetime.core.timer import FTLoopTimer
FTLoopTimer(0.1, 0, _main).start()
# 重置充点小钱（首充豪礼）SERVERIDS填写:UT9999000001


# 召唤指定鱼阵
# 测试服：GT00280011001,GT00280021001,GT00280021002,GT00280031001,GT00280041001,GT00280081001,GT00280081002,GT00280081003,GT00280091001,GT00280091002,GT00280141001
# 仿真服：GT00280011001,GT00280011002,GT00280011003,GT00280011004,GT00280011005,GT00280011006,GT00280021001,GT00280021002,GT00280021003,GT00280021004,GT00280022001,GT00280022002,GT00280022003,GT00280022004,GT00280031001,GT00280031002,GT00280031003,GT00280031004,GT00280031005,GT00280031006,GT00280041001,GT00280041002,GT00280041003,GT00280041004,GT00280041005,GT00280041006,GT00280051001,GT00280061001,GT00280071001,GT00280081001,GT00280081002,GT00280081003,GT00280081004,GT00280081005,GT00280081006,GT00280081007,GT00280081008,GT00280081009,GT00280091001,GT00280091002,GT00280091003,GT00280091004,GT00280091005,GT00280091006,GT00280091007,GT00280091008,GT00280091009,GT00280091010,GT00280091011,GT00280141001,GT00280141002,GT00280141003,GT00280141004,GT00280141005,GT00280141006
fishId = 1701
fishGroupType = {
    1302: "boss_201",       # 八爪鱼
    1304: "boss_301",       # 美人鱼
    1305: "binglong_301",   # 冰龙
    1306: "boss_203",       # 圣天使
    1307: "boss_204",       # 堕天使
    1308: "boss_501",       # 七彩云鲲
    1309: "boss_502",       # 道墟古鲲
    1310: "boss_222",       # 巨型灯笼鱼
    1502: "boss_huofenghuang",  # 火凤凰
    1504: "boss_anyejushou",    # 暗夜炬兽
    1707: "boss_wuseshenniu",   # 五色神牛
    1708: "boss_sunwukong",     # 孙悟空
    1709: "boss_zhubajie",      # 猪八戒
    1710: "boss_nezha",         # 哪吒
    1711: "boss_tiesuoelong",   # 铁锁恶龙
    1402: "shandianyu_01",      # 闪电鱼
    1403: "zhadanyu_01",        # 炸弹鱼
    1404: "yiwangdajin_1404",   # 一网打尽红尾鲶
    1405: "yiwangdajin_1405",   # 一网打尽灯笼鱼
    1406: "yiwangdajin_1406",   # 一网打尽蓝蝠鲼
    1408: "zuanshibaoxiang_01", # 钻石宝箱
    1409: "zuantouxie_01",      # 钻头蟹
    1410: "rulaishenzhang_01",  # 如来神掌
    1411: "lianhuanzhadanxie_01",   # 炸弹蟹
    1412: "leishenchuixie_01",  # 雷神锤
    1501: "boss_jinzhu",        # 金猪
    1503: "fortuneBoss",        # 财神
    1505: "boss_shengdanlaoren",# 圣诞老人
    1701: "longwang_401",       # 黄金龙王
    1413: "shanggujianxia_01",  # 斩妖剑
    1414: "xianshi_zhounianqing",   # 如意袋
    1415: "xianshi_huanlexiaochou", # 欢乐小丑
    1506: "boss_xingzuo_baiyangzuo",# 白羊座
    1507: "boss_xingzuo_jinniuzuo"  # 金牛座  
}

def _main():
    from poker.entity.configure import gdata
    for _, room in gdata.rooms().iteritems():
        for _, table in room.maptable.iteritems():
            if fishId == 1701:
                hasattr(table, "dragonKing") and table.dragonKing and table.dragonKing.bossStart(isCall=True)
            elif fishId == 1501:
                hasattr(table, "goldenPig") and table.goldenPig and (table.goldenPig.actEnd() or table.goldenPig.goldPigStart())
            elif fishId in [1503, 1505]:
                from freetime.entity.msg import MsgPack
                msg = MsgPack()
                msg.setParam("groupId", fishGroupType[fishId])
                table._insertFortuneBoss(msg)
            elif fishId == 1305:
                if hasattr(table, "dragonBoss") and table.dragonBoss:
                    group = table.insertFishGroup(fishGroupType[fishId], tgGroupId=fishGroupType[fishId])
                    table.dragonBoss.dragonBossGroup = group
                    table.dragonBoss.iceDragonStart()
            elif fishId in fishGroupType:
                table.insertFishGroup(fishGroupType[fishId], tgGroupId=fishGroupType[fishId])

from freetime.core.timer import FTLoopTimer
FTLoopTimer(0.1, 0, _main).start()
# 召唤指定鱼阵

# 炮台砍价完成所有任务，SERVERIDS填写:UT9999000001
from poker.entity.dao import daobase
from fish.entity.activities import battery_bargain

def _main():
    userId = 11721
    # daobase.executeUserCmd(userId, "del", battery_bargain._getRedisKey(userId))
    # battery_bargain.initTaskData(userId)
    for taskId in battery_bargain.nb_conf.get("taskConf", {}).get("tasks", {}):
        battery_bargain._setTaskState(userId, int(taskId), 1)

from freetime.core.timer import FTLoopTimer
FTLoopTimer(0.1, 0, _main).start()
# 炮台砍价完成所有任务，SERVERIDS填写:UT9999000001

# 捕鱼掉落卡册卡片、卡包，SERVERIDS填写:
# 测试服：GT00280011001,GT00280021001,GT00280031001,GT00280041001,GT00280081001,GT00280081002,GT00280091001,GT00280141001
# 仿真服：GT00280011001,GT00280011002,GT00280011003,GT00280011004,GT00280011005,GT00280011006,GT00280011007,GT00280011008,GT00280021001,GT00280021002,GT00280021003,GT00280021004,GT00280021005,GT00280021006,GT00280021007,GT00280022001,GT00280022002,GT00280022003,GT00280022004,GT00280022005,GT00280022006,GT00280022007,GT00280031001,GT00280031002,GT00280031003,GT00280031004,GT00280031005,GT00280031006,GT00280031007,GT00280031008,GT00280041001,GT00280041002,GT00280041003,GT00280041004,GT00280041005,GT00280041006,GT00280051001,GT00280061001,GT00280071001,GT00280081001,GT00280081002,GT00280081003,GT00280081004,GT00280081005,GT00280081006,GT00280081007,GT00280081008,GT00280081009,GT00280081010,GT00280091001,GT00280091002,GT00280091003,GT00280091004,GT00280091005,GT00280091006,GT00280091007,GT00280091008,GT00280141001,GT00280141002,GT00280141003,GT00280141004,GT00280141005,GT00280141006
from fish.entity import card_book

def card_book_drop_handler(self, value, multiple):
    obj = card_book.main_obj
    if not obj:
        return
    return obj.card_book_drop_handler(self.userId, 1800000, 10000000, multiple)

from fish.table.player import FishPlayer
FishPlayer.card_book_drop_handler = card_book_drop_handler
# 捕鱼掉落卡册卡片、卡包