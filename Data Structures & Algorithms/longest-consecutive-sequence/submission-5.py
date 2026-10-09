class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_seq = 1
        st = set()
        for num in nums:
            st.add(num)
        
        seq = 1
        for i in range(len(nums)):
            if nums[i] not in st:
                continue
            right = nums[i]
            left = nums[i]
            st.remove(nums[i])
            while right+1 in st:
                right += 1
                st.remove(right)
            while left-1 in st:
                left -= 1
                st.remove(left)
            seq = right - left + 1
            if seq > longest_seq:
                longest_seq = seq
            seq = 1

        return longest_seq




        