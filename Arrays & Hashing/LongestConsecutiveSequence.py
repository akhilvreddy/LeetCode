from ast import List

class Solution: 
    def LongestConsecutiveSequence(self, nums:List[int]) -> int: 

        numsSet = set(nums)
        maxFloater = 0

        for number in nums: 
            if (number-1) not in numsSet: 
                currFloaterLength = 1
                while ((number + currFloaterLength) in numsSet):
                    currFloaterLength = currFloaterLength + 1
                maxFloater = max(maxFloater, currFloaterLength)
        
        return maxFloater