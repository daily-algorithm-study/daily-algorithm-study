class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def movingOneBlock(arr, start):
            for i in range(len(arr) - 1, start, -1):
                arr[i] = arr[i - 1]

        nums1Length = m
        for number2 in nums2:
            for i, number1 in enumerate(nums1):
                if i >= nums1Length:
                    nums1[i] = number2
                    nums1Length += 1
                    break
                elif number1 >= number2:
                    movingOneBlock(nums1, i)
                    nums1[i] = number2
                    nums1Length += 1
                    break



