class Solution: 
    def isPalindrome(self, s:str) -> bool: 
        l, r = 0, len(s)-1 

        while (l < r): 
            
            while l < r and not self.isAlphaNumeric(s[l]):
                l = l + 1

            while r > l and not self.isAlphaNumeric(s[r]):
                r = r - 1

            if (s[l].lower() != s[r].lower()):
                return False
            
            l = l + 1
            r = r - 1
        
        return True
      
    def isAlphaNumeric(self, c) -> bool:     
        if (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')): 
            return True
        return False 