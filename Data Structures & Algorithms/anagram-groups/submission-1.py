class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = {}
            for char in word:
                count[char] = count.get(char,0) + 1
            
            key = tuple(sorted(count.items()))
            
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())
        