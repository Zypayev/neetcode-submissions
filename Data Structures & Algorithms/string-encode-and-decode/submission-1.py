class Solution:

    def encode(self, strs: List[str]) -> str:
        hints = ""
        hints += str(len(strs)) + " "
        encoded = ""
        for word in strs:
            hints += str(len(word)) + " "
            encoded += word
        return hints+encoded

    def decode(self, s: str) -> List[str]:
        count = ""
        pin = 0
        for i in range(len(s)):
            if s[i] == " ":
                pin = i + 1
                break
            count += s[i]
            i += 1
        count = int(count)
        lengths = []
        length = ""
        for i in range(pin, len(s)):
            if s[i] == " ":
                if count <= 1:
                    lengths.append(int(length))
                    pin = i + 1
                    break
                else:
                    lengths.append(int(length))
                    count -= 1
                    length = ""
            else:
                length += s[i]
            
            i += 1
        words = []
        
        for i in range(len(lengths)):
            words.append(s[pin:pin+lengths[i]])
            pin += lengths[i]
        
        return words


                    
        
                    
            



