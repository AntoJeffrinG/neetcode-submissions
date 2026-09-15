class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2)-len(s1)+1):
            key = ""
            for j in range(i,i+len(s1)):
                key += s2[j]
                if len(key) == len(s1):
                    if sorted(key) == sorted(s1):
                        return True
                    break
        return False
        