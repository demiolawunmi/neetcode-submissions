class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            temp = {}

            for char in word:
                if char in temp:
                    temp[char] += 1
                else:
                    temp[char] = 1

            key = tuple(sorted(temp.items()))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        
        return list(groups.values())
            


