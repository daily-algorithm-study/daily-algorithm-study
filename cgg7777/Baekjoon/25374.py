class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        answer = -1
        left = 0
        right = 10000001
        while (left <= right):
            mid = (left + right) // 2
            if mid == 0: break
            sumValue = 0.0
            for j in range(len(dist)):
                if (j == len(dist) - 1):
                    sumValue += dist[j] / mid
                else:
                    sumValue += -((-dist[j]) // mid)
            if sumValue <= hour:
                answer = mid
                right = mid -1
            else:
                left = mid +1
        return answer