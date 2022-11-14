class Solution: 
    def validAnagram(self, s: str, t: str) -> bool: 
        
        if (len(s) != len(t)):  # if lengths are not the same, they cannot be anagrams
            return False 

        countS, countT = {},{} # creating hashmaps in python

        for i in range(len(s)): # iterate through the string
            countS[s[i]] = 1 + countS.get(s[i], 0) # increment counter of character s[i]
            countT[t[i]] = 1 + countT.get(t[i], 0) # increment counter of character t[i]
            
        return countS == countT # return if both of the hashmaps are equivalent to each other (meaning valid anagrams)