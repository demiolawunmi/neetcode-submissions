class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = []
        total = 1
        zeroCount = 0

        for num in nums:
            if num != 0:
                total *= num
            else:
                zeroCount += 1

        for num in nums:
            if zeroCount > 1:
                newList.append(0)
            elif zeroCount == 1:
                newList.append(total if num == 0 else 0)
            else:
                newList.append(total // num)

        return newList
