from ast import List

class Solution: 
    def TopKFrequent (self, nums: List[str], k:int) -> List[int]:

        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for n in nums: 
            count[n] = count.get(n, 0) + 1
        for n, c in count.items:
            frequency[c].append(n)

        result = []
        for i in range(len(frequency), 0, -1):
            for n in frequency[i]: 
                result.append(n)
                if len(result) == k: 
                    return result