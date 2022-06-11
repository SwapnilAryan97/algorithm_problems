class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = -prices[0]
        b = float('-inf')
        c = float('-inf')
        d = float('-inf')
        
        for price in prices:
            a = max(a, -price)
            b = max(b, a+price)
            c = max(c, b-price)
            d = max(d, c+price)
        return d