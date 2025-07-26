class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = [item[0]for item in items[:k]]
        return result
