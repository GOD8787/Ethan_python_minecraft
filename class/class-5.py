# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:52:33 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
while True: 
    time.sleep(1)
    x,y,z = mc.player.getTilePos()
    mc.postToChat('You are located on X:'+ str(x)+"Y:"+str(y)+"Z:"+str(z))