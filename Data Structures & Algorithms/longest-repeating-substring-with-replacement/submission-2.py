class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        freq = {s[0]:1}
        left = 0
        max_freq = 1
        max_len = 1
        for right in range(1,len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_freq = max(max_freq,freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max(0,max_len)
            
        