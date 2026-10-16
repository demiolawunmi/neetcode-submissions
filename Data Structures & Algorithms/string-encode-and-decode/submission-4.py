class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""

        for word in strs:
            temp += str(len(word)) + "#" + word
        
        return(temp)

    def decode(self, s: str) -> List[str]:
        newList = []
        i = 0

        while (i < len(s)):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            newList.append(s[j + 1:j + 1 + length])
            
            i = j + 1 + length

        return newList



