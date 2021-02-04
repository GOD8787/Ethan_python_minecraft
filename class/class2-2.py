# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:25:14 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import random
import time
x,y,z = mc.player.getTilePos() 
while True:
    time.sleep(1)
    color = random.randint(0,15)    
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35,color)