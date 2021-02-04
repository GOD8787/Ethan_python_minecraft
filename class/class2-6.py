# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:16:19 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
username = input("username?")
message = input()
mc.postToChat("<"+username+"> "+message)