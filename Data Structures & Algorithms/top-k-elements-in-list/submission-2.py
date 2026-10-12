class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        return [freq[0] for freq in sorted(dic.items(), key=lambda item: item[1])[-k:]]
            

        