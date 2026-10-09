class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        total = 1
        zero_count = zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                if zero_count < 2:
                    zero_index = i
                else:
                    return [0 for _ in range(len(nums))]
                continue
            total *= nums[i]

        if zero_count == 1:
            output = [0 for _ in range(len(nums))]
            output[zero_index] = total
            return output
        
        output = []
        for num in nums:
            output.append(total//num)

        return output

        