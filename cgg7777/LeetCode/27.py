class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k +=1

        for i in range(len(nums)):
            if nums[i] != -1:
                currentIndex = i
                while currentIndex >= 1 and nums[currentIndex-1] == -1:
                    nums[currentIndex-1], nums[currentIndex] = nums[currentIndex], nums[currentIndex-1]
                    currentIndex -= 1
        for i in range(len(nums)-k, len(nums)):
            nums[i] = '_'
        return len(nums)-k