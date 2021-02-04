# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:56:56 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
while True:
    x,y,z= mc.player.getPos()
    mc.setBlock(x,y+2,z,8)
    time.sleep(0.01)