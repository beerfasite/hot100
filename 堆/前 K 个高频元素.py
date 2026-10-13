class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())

        buckets = [[] for _ in range(max_cnt + 1)]
        for x,c in cnt.items():
            buckets[c].append(x)
        
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans



"""
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for num, freq in cnt.items():
            heapq.heappush(heap, (freq, num))
            # 堆超过k个,弹出频次最小的
            if len(heap) > k:
                heapq.heappop(heap)
        # 取出堆里面所有数字
        res = [item[1] for item in heap]
        return res

"""