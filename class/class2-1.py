# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:09:14 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
h = 5
w = 5
mc.setBlocks(x,y,z,x+w,y+h,z+w,1)
mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+w-1,0)