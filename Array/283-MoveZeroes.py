class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)): 
            if nums[i] == 0:
                nums = nums[0:i] + nums[i+1:] + [0]
                
        