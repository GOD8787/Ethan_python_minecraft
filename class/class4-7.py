# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:10:17 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
ID = mc.getPlayerEntit("xXGODXx8787")
mc.postToTitle(ID,"hello")