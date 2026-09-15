class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''for i in range(len(s2)-len(s1)+1):
            key = ""
            for j in range(i,i+len(s1)):
                key += s2[j]
                if len(key) == len(s1):
                    if sorted(key) == sorted(s1):
                        return True
                    break
        return False'''

        count1 = {}
        count2 = {}

        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i],0) + 1

        left = 0
        for right in range(len(s2)):
            count2[s2[right]] = count2.get(s2[right],0) + 1

            if (right-left+1) > len(s1):
                old = s2[left]
                count2[s2[left]] -= 1

                if count2[s2[left]] == 0:
                    del count2[old]
                left += 1

            if count1 == count2:
                return True
        return False

        