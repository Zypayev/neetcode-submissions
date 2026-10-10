class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        triplets = set()
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                k = -(nums[i]+nums[j])
                if k in dic:
                    if dic[k] != i and dic[k] != j:
                        triplets.add(tuple(sorted([nums[i], nums[j], k])))

        return list(triplets)


        