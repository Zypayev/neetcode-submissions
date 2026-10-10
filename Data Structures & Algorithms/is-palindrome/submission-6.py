class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for letter in s:
            if letter >= 'A' and letter <= 'Z' or letter >= 'a' and letter <= 'z' or letter >= '0' and letter <= '9':
                clean_str += letter
        
        clean_str = clean_str.lower()
        str_length = len(clean_str)
        print(clean_str)
        middle = str_length//2
        for i in range(middle):
            if clean_str[i] != clean_str[str_length-1-i]:
                return False
        return True
