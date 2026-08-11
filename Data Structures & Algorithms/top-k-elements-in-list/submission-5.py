class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))

        res = []
        i = 0
        for keys in sorted_freq.keys():
            res.append(keys)
            i += 1
            if i == k:
                return res


        



        