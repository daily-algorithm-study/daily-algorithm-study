class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        answer = 0
        accArr = [0 for _ in range(len(nums)+1)]
        for i, num in enumerate(nums):
            accArr[i+1] = accArr[i] + num

        left = 1
        right = len(nums)
        while left <= right:
            length = (left + right)//2
            satisfiedFlag = False
            for i in range(0, len(nums)-length+1):
                if accArr[i+length] - accArr[i] >= target:
                    satisfiedFlag = True
                    if answer == 0 or length < answer:
                        answer = length
            if satisfiedFlag:
                right = length -1
            else:
                left = length+1

        return answer

