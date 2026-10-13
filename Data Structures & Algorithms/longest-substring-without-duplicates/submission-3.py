class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0
        for i, l in enumerate(s):
            if l in seen:
                longest = max(longest, i-start)
                start = max(start, seen[l]+1)
            seen[l] = i
            
        return max(longest, len(s)-start)