class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(index,path):
            if index == len(s):
                result.append(path.copy())
                return
            
            for i in range(index,len(s)):
                if is_palindrome(index,i):
                    path.append(s[index:i+1])
                    backtrack(i+1,path)
                    path.pop()
            
        def is_palindrome(start,end):
            l,r = start,end
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        result = []
        backtrack(0,[])
        return result
        