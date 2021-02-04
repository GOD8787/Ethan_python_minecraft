# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:12:41 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()   
def planttree(x,y,z,mc):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,35,5)
    mc.setBlocks(x,y+4,z,x,y,z,17)
for i in range(0,10):
    for h in range(0,10):
        for j in range(0,10):
            planttree(x+i*5,y+i*5,z+i*j,mc)