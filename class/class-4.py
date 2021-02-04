# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:55:53 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
t = 0
while t < 100:
    time sleep(0.5)
    mc.postToChat("t = "+str(t))
    t = t+1