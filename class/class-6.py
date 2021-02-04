# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:21:46 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,46) #前
mc.setBlock(x-1,y,z,46) #後
mc.setBlock(x,y,z+1,46) #左
mc.setBlock(x,y,z-1,46) #右
mc.setBlock(x,y,z+1,46) #右上
mc.setBlock(x-1,y,z-1,46) #左下
mc.setBlock(x+1,y,z-1,46)# 左上
mc.setBlock(x-1,y,z+1,46)# 右下