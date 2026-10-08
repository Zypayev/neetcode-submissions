class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appearance = {}
        for num in nums:
            if num not in appearance:
                appearance[num] = 0
            appearance[num] += 1
        top = []
        max = value = 0
        
        for _ in range(k):
            for key, frequency in appearance.items():
                if frequency > max:
                    max = frequency
                    value = key
            max = 0
            appearance.pop(value)
            top.append(value)
        
        return top
            

        