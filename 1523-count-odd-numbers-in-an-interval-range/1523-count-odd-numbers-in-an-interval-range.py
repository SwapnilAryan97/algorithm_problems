class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if int(str(low)[-1])%2==1 or int(str(high)[-1])%2==1:
            return ((high-low)//2) + 1
        else:
            return ((high-low)//2)