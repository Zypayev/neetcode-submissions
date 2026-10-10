class Solution:
    def isPalindrome(self, s: str) -> bool:
        legit_length = 0
        for letter in s:
            if letter >= 'A' and letter <= 'Z' or letter >= 'a' and letter <= 'z' or letter >= '0' and letter <= '9':
                legit_length += 1
        
        middle = legit_length//2
        i = 0
        j = len(s)-1
        while i < middle and j >= middle:
            letter_left = s[i]
            while (letter_left < 'A' or letter_left > 'Z') and (letter_left < 'a' or letter_left > 'z') and (letter_left < '0' or letter_left > '9'):
                i += 1
                if i >= middle:
                    break            
                letter_left = s[i]
            
            letter_right = s[j]
            while (letter_right < 'A' or letter_right > 'Z') and (letter_right < 'a' or letter_right > 'z') and (letter_right < '0' or letter_right > '9'):
                j -= 1
                if j < middle:
                    break             
                letter_right = s[j]
            
            if j < middle or i >= middle:
                return True   
            
            if letter_right.lower() != letter_left.lower():
                return False
            i += 1
            j -= 1
            
        return True
