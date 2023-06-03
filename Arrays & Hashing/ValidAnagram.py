class Solution: 
    def isAnagram(self, s:str, t:str) -> bool: 

        if (len(s) != len(t)): 
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            x = s[i]
            y = t[i]

            countS[x] = countS.get(x, 0) + 1
            countT[y] = countT.get(y, 0) + 1

        for c in countS: 
            if countS[c] != countT.get(c, 0): 
                return False
        
        return True