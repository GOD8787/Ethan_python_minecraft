# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:53:55 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,5,"I Love", "Minecraft", "and", "Python")