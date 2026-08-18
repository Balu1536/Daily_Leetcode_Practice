from collections import defaultdict
from typing import List


class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = defaultdict(int)

        # Count in how many distinct subarrays of size k each number appears
        for i in range(n - k + 1):
            window_elements = set(nums[i : i + k])
            for num in window_elements:
                subarray_count[num] += 1

        # Find the largest integer that appears in exactly 1 subarray
        ans = -1
        for num, count in subarray_count.items():
            if count == 1:
                ans = max(ans, num)

        return ans