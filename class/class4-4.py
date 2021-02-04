# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:02:26 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
from time import sleep
mc = mcs.create()
while True:
    sleep(0.2)
    mc.executeCommand("time add 300")


