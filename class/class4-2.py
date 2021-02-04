# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:44:36 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
number = 1
for i in range(8):
    time.sleep(1)
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number * 2
    mc.postToChat(str(number))
