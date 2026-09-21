class Solution:
    # O(n + k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = {}
        # O(n)
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        
        buckets = [[] for _ in range(n + 1)]
        
        # O(n)
        for key, freq in freqs.items():
            buckets[freq].append(key)


        # O(k)
        res = []
        curr_bucket = []
        while len(res) < k:
            if len(curr_bucket) == 0:
                curr_bucket = buckets.pop()
            else:
                res.append(curr_bucket.pop())
        
        return res


