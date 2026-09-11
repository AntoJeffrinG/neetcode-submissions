class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqS = {}
        freqT = {}
        for i in t:
            freqT[i] = freqT.get(i,0) + 1

        need = len(freqT)
        have = 0

        min_len =float('inf')

        left = 0
        for right in range(len(s)):
            freqS[s[right]] = freqS.get(s[right],0) + 1

            if s[right] in freqT and freqS[s[right]] == freqT[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start = left
                    end = right
                
                freqS[s[left]] -= 1
                if s[left] in freqT and freqS[s[left]] < freqT[s[left]]:
                    have -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[start:end+1]
        