# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:19:22 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import random
mc = mcs.create()
x,y,z = mc.player.getTilePos()
Blen = 4
for j in range(5):
    for i in range(5):
        num = random.randint(1,6)
        if num == 1:
            mc.setBlocks(x,y,z,x+Blen,y,z,1)
            x = x + Blen
        elif num == 2:
            mc.setBlocks(x,y,z,x-Blen,y,z,1)
            x = x - Blen
        elif num == 3:
            mc.setBlocks(x,y,z,x,y,z+Blen,1)
            z = z + Blen
        elif num == 4:
            mc.setBlocks(x,y,z,x,y,z-Blen,1)
            z = z - Blen
        elif num == 5:     
            mc .setBlocks(x,y,z,x,y+Blen,z,1)
            y = y + Blen
        elif num == 5:     
            mc .setBlocks(x,y,z,x,y-Blen,z,1)
            y = y - Blen    
            