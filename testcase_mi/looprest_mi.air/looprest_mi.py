# -*- encoding=utf8 -*-
__author__ = "Hyper"
import sys
import codecs
import traceback

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common_airtest.common_airtest_all import *


def looprest_mi():
    login_mi()
    looprest()
    #touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986707484.png", threshold=0.8, record_pos=(-0.08, -0.002), resolution=(2700, 1228)))
    touch(Template(r"tpl1659511988577.png", record_pos=(0.043, 0.07), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986730917.png", threshold=0.8, record_pos=(0.046, -0.002), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512015562.png", record_pos=(0.158, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986751994.png", record_pos=(0.176, -0.003), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512042281.png", record_pos=(0.155, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    swipe(Template(r"tpl1656986814966.png", record_pos=(0.177, -0.002), resolution=(2700, 1228)), vector=[-0.4977, 0.0258])
    #touch(Template(r"tpl1656986876169.png", record_pos=(-0.134, -0.001), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512068508.png", record_pos=(-0.117, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986901130.png", record_pos=(-0.005, -0.003), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512084946.png", record_pos=(-0.004, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986925259.png", record_pos=(0.122, -0.003), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512097565.png", record_pos=(0.107, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))
        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    #touch(Template(r"tpl1656986942153.png", record_pos=(0.249, -0.001), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512114991.png", record_pos=(0.225, 0.072), resolution=(2400, 1080)))

    sleep(10)
    if exists(Template(r"tpl1657163237002.png", record_pos=(0.084, -0.097), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163247672.png", record_pos=(-0.439, -0.165), resolution=(2400, 1080)))
        sleep(2)
        touch(Template(r"tpl1657262045961.png", record_pos=(-0.129, 0.128), resolution=(2400, 1080)))

        sleep(5)
        touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
        sleep(5)
    if exists(Template(r"tpl1657003690951.png", record_pos=(0.284, -0.13), resolution=(2700, 1228))):
        touch(Template(r"tpl1657003690951.png", record_pos=(0.284, -0.13), resolution=(2700, 1228)))
    sleep(2)
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
        
        
if __name__=='__main__':
    looprest_mi()