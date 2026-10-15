class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        counts2 = {}
        
        for char in s:
            match (char not in counts1, char in counts1):
                case (True, False):
                    counts1[char] = 1
                case (False, True):
                    counts1[char] += 1
        
        for char in t:
            match (char not in counts2, char in counts2):
                case (True, False):
                    counts2[char] = 1
                case (False, True):
                    counts2[char] += 1
        
        if counts1 == counts2:
            return True
        return False
            
            