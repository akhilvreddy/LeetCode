from typing import List

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:

        myHashSet = set() # initialize a hashset to store values
              
        for n in nums: # iterate through the array
            if n in myHashSet: 
                return True # return true if value was already found
            myHashSet.add(n) # add value if it was not found yet
                
        return False # if no repeated values were found, return false