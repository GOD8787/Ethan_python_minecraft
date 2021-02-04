# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:46:06 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
import random
mc = mcs.create()
while True:
    x,y,z = mc.player.getPos()
    time.sleep(1)
    x = x+random.uniform(1,30)
    y = y+random.uniform(1,30)
    z = z+random.uniform(1,30)
    mc.spawnEntity(x+1,y,z,93)
