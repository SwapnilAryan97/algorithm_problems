class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k = len(nums)-1
            while j<k:
                val = nums[i]+nums[j]+nums[k]
                if abs(target-val)<abs(diff):
                    diff = target-val 
                if val<target:
                    j+=1
                else:
                    k-=1
            if diff==0:
                break 
        
        return target-diff