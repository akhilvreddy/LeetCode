from typing import List

class Solution: 
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        
        myHashMap = {} # instantiating a hashmap in python, going to map from value to index
        
        for i, n in enumerate(nums):  # i is the index, n is the value 
            difference = target - n # value of number we are looking for
            if difference in myHashMap: # if the value we are looking for is in the hashmap, then return the answer
                return [myHashMap[difference], i] # return original index with our current index ## return [i, myHashMap[difference]] also works
            myHashMap[n] = i # set hashmap value to specific index