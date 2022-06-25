class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res, n = 0, len(piles)
        for i in range(n//3, n, 2):
            res+= piles[i]
        return res