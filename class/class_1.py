# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:36:06 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs 
mc = mcs.create()
mc.player.setTilePos(1000, 100,1000)
print(mc.player.getTilePos())