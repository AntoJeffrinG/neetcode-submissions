class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [-1] * (n+1)
        def help(n,arr):
            if n == 0:
                return arr[n]
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            pick = arr[n] + help(n-2,arr)
            n_pick = 0 + help(n-1,arr)
            
            dp[n] = max(pick, n_pick)
            return dp[n]

        arr_1 = nums[:n-1]
        arr_2 = nums[1:]

        res_a = help(len(arr_1) - 1,arr_1)
        for i in range(len(dp)):
            dp[i] = -1

        res_b = help(len(arr_2) - 1,arr_2)

        return max(res_a,res_b)
        