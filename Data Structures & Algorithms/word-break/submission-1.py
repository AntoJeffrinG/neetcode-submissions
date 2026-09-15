class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def check(start):
            if start == len(s):
                return True
            
            if dp[start] != -1:
                return dp[start]

            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in wordDict:
                    if check(end):
                        dp[start] = True
                        return dp[start]
            dp[start] = False
            return dp[start]
        
        dp = [-1] * len(s)
        return check(0)
        