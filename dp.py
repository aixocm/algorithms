#!/usr/bin/python
#-*- coding:utf-8 -*-
def maxBag(weight, value, totalWeight):
    if len(weight) <= 0 or len(value) <= 0 or totalWeight <= 0 or len(weight) != len(value):
            return
	        num = len(weight)
		    tempMat = []
		        for i in range(num+1):
			        tempMat.append([0]*(totalWeight+1))
				    for j in range(1, totalWeight+1):
				            for i in range(1,num+1):
					                if j - weight[i-1] >= 0:
							                tempMat[i][j] = max(tempMat[i-1][j], value[i-1] + tempMat[i-1][j-weight[i-1]])
									            else:
										                    tempMat[i][j] = tempMat[i-1][j]
												        return tempMat[-1][-1]

													weight, value, totalWeight = [2,1,3,2], [12,10,20,15], 5
													print(maxBag(weight, value, totalWeight))
