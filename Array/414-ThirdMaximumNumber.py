import math
class Solution:
    def thirdMax(self, nums):
        maxNum = float("-inf")
        scmaxNum = float("-inf")
        thmaxNum = float("-inf")
        for num in nums: 
            if num > maxNum: 
                thmaxNum = scmaxNum
                scmaxNum = maxNum
                maxNum = num 
            elif num>scmaxNum and num!=maxNum: 
                thmaxNum = scmaxNum
                scmaxNum = num
            elif num>thmaxNum and num!=scmaxNum and num!=maxNum: 
                thmaxNum = num 
        if thmaxNum ==float("-inf"): 
            return maxNum
        else: 
            return thmaxNum