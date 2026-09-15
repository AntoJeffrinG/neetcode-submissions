class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i,path):
            if i == len(digits):
                result.append(''.join(path))
                return
            
            letter = phone[digits[i]]

            for c in letter:
                path.append(c)
                backtrack(i+1,path)
                path.pop()
        
        result = []
        backtrack(0,[])
        return result