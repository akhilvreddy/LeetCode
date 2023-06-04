from ast import List
import collections

class Solution: 
    def GroupAnagram(self, theList:List[str]) -> List[[List[str]]]: 

        mainHashMap = collections.defaultdict(list)

        for aString in theList: 
            count = [0] * 26
            for character in aString: 
                count[ord(character)-ord('a')] += 1
            mainHashMap[tuple(count)].append(aString)

        return mainHashMap.values()