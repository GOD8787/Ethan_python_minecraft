# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:17:15 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()
for i in range(50):
    mc.setBlock(x+i,y,z,1)

