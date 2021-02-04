# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:37:26 2021

@author: USER
"""
A = [10,25,31,2,4,6,99,-1,34]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] > A [j]:
            t = A[i]
            A[i] = A[j]
            A[j] = t
            print(A)