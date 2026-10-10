class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        triplets = []
        nums = sorted(nums)
        left, middle, right = 0,1, len(nums)-1
        
        while left < right and nums[left] < 1:
            while middle < right:
                diff = -(nums[left]+nums[middle])
                while middle < right:
                    if nums[right] == diff:
                        triplets.append([nums[left], nums[middle], nums[right]])
                    if nums[right] < diff:
                        break
                    right -= 1
                    while nums[right] == nums[right+1]:
                        right -= 1
                        if right == -1:
                            return triplets
                middle += 1
                while nums[middle] == nums[middle-1]:
                    middle += 1
                    if middle == len(nums):
                        return triplets
            
            left += 1
            while nums[left] == nums[left-1]:
                left += 1
                if left == len(nums):
                    return triplets
            middle = left + 1
            right = len(nums)-1
        
        return triplets


        