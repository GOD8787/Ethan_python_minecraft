# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:19:01 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x , hit.pos.y , hit.pos.z
        mc.player.setPos()
