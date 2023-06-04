from ast import List

class Solution: 
    def TwoSum(self, nums:List[int], target:int) -> bool: 

        hashmap = {} 

        # key is going to be target - value
        # value is going to be index

        for index, value in enumerate(nums): 
            
            difference = target - value
            if difference in hashmap: 
                return [index, hashmap[difference]]
            else: 
                hashmap[difference] = index