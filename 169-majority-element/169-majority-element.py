class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mem = {}
        res = float('-inf')
        temp = 0
        n = len(nums)
        for num in nums:
            if num not in mem:
                mem[num] = 1
            else:
                mem[num] += 1
            if mem[num]>=n//2:
                if mem[num]>temp:
                    res = num
                    temp = mem[num]

            # temp = max(mem[num], temp)
            # print(temp)
            
#             if mem[num]>temp:
#                 res = num
#                 temp = mem[num]
            
        return res