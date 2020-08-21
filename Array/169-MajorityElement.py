class Solution:
    def majorityElement(self, nums):
        seen={}
        for num in nums: 
            if num not in seen.keys(): 
                seen[num]=1 
            else: 
                seen[num]+=1 
        max1 = max(seen.values())
        for key in seen.keys(): 
            if seen[key]==max1: 
                return key 