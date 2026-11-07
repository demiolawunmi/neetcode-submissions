class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        numSet = set(nums)
        print(numSet)

        longest = 0
        

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                
                while num + count in numSet:
                    count += 1
            
                longest = max(longest, count)
        
        
        return longest