from ast import List

class Solution: 
    def TwoSumII(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1 

        while l < r: 
            
            currentSum = nums[l] + nums[r]
        
            if (currentSum > target): 
                r = r - 1
            elif (currentSum < target):
                l = l + 1
            else: 
                return [l+1, r+1]
            
        return []