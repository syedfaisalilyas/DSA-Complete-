# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:06:07 2023

@author: JUNCTION
"""

A = [[1,4],[2,5],[7,9],[9,10],[6,10]]

arr = [[0,0],[0,0],[0,0],[0,0],[0,0]]
def SelectionSort(array,start,end):
    for i in range(0,len(A)):
        for j in range(0,1):
            

            if A[i][j] <= A[i-1][j+1] and A[i][j+1]>= A[i-1][j]  :
              arr[i][j] = i
              arr[i][j+1] = i+1
    
    return arr

print(len(A[0]))
print(SelectionSort(A,0,len(A)-1))