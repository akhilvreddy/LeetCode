from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # lets see what we can put here
        
        return True



# Logic:

# you are going to create a hashmap, keys are going to be "counters" eachw word
# and the values would be the words themselves

# hence, for a single key, all the values would be the anagrams

# Pseudocode: 

# loop through the list once, for each word in the list
# create an array to hold the counter (size of 26)
# now, for values with that counter in the array, add value to the key
# once for loop finishes, we are good