class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = sorted((nums1,nums2), key=len)
        m,n = len(a), len(b)
        low, high = 0,m
        after = int((m+n-1)/2)
        while low<high:
            i = int((low+high)/2)
            if after-i-1<0 or a[i]>=b[after-i-1]:high = i
            else:low = i+1
        i=low
        nextfew = sorted(a[i:i+2]+b[after-i:after-i+2])
        return (nextfew[0]+nextfew[1-(m+n)%2])/2