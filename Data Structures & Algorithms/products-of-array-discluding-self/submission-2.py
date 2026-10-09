class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        left = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]

        right = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        output = []
        for i in range(len(nums)):
            output.append(left[i]*right[i])

        return output

        