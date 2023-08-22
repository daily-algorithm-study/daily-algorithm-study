class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        before = -1
        intervalArray = []
        for interval in intervals:
            if before == -1:
                before = interval
            else:
                if before[1] >= interval[0]:
                    before = [min(before[0], interval[0]), max(before[1], interval[1])]
                else:
                    intervalArray.append(before)
                    before = interval

        if before != -1:
            intervalArray.append(before)
        return intervalArray