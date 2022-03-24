class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        # print(dp)
        for c in candidates:
            for i in range(c, target+1):
                if i==c:
                    dp[i].append([c])
                for combo in dp[i-c]:
                    # print('combo=',combo)
                    dp[i].append(combo + [c])
            # print(dp)
        return dp[-1]