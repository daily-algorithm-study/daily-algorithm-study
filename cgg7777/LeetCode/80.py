class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        REMOVED = -1000000
        removedCount = 0
        countNum = {}
        for i, entry in enumerate(nums):
            if entry in countNum:
                countNum[entry] +=1
                if countNum[entry] >= 3:
                    nums[i] = REMOVED
                    removedCount +=1
            else:
                countNum[entry] = 1

        for i in range(len(nums)):
            if nums[i] != REMOVED:
                currentIndex = i
                while currentIndex >= 1 and nums[currentIndex-1] == REMOVED:
                    nums[currentIndex-1], nums[currentIndex] = nums[currentIndex], nums[currentIndex-1]
                    currentIndex -= 1
        k = len(nums) - removedCount
        return k