# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:47:01 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
from time import sleep
import random
mc = mcs.create()
ID = mc.getPlayerEntityId("easonku")
while True:
    sleep(1)
    x,y,z = mc.entity.getTilePos(ID)
    mineral = [14,15,16,56,73,129]
    style = random.choice(mineral)
    mc.setBlock(x,y,z,mineral)