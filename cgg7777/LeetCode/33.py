class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = nums[0]
        while (left <= right):
            mid = (left + right) // 2
            current = nums[mid]
            if target < current and ((pivot <= current and pivot <= target) or (pivot > current and pivot > target)):
                right = mid - 1
            elif target < current:
                left = mid + 1
            elif target > current and ((pivot <= current and pivot <= target) or (pivot > current and pivot > target)):
                left = mid + 1
            elif target > current:
                right = mid - 1
            elif target == current:
                right = mid
                break
        if nums[right] == target:
            return right
        else:
            return -1

