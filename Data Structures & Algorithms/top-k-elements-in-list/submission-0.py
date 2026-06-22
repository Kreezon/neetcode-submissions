class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for n in nums:
            if n in store:
                store[n] += 1
            else:
                store[n] = 1

        sorted_items = sorted(store.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result