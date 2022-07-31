from typing import List
from heapq import heappush, nlargest

# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1

        for num in freq:
            heappush(heap, (freq[num], num))
        return [val[1] for val in nlargest(k, heap)]


if __name__ == "__main__":
    res = Solution().topKFrequent([1,1,1,2,2,3], 2)
    print(res)
