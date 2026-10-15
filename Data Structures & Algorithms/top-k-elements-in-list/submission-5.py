class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        mode = []

        for num in nums:
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1
        
        for num, count in hMap.items():
            freq[count].append(num)
            
        for item in reversed(freq):
            for num in item:
                if len(mode) < k:
                    mode.append(num)
                else:
                    return(mode)
        
        return(mode)

