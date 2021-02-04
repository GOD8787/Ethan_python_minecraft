# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:14:53 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
from random import randint
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
com = randint(0,15) 
for i in range(16):
    for j in range(16):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if com == data:
            mc.postToChat("You are win")
            break
        else:
            mc.postToChat("Try again")
        if com > data:    
            mc.postToChat("Too big")
        if com < data:
            mc.postToChat("Too small")
            
            
    
        