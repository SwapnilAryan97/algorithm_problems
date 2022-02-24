class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        start_idx = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]]+1)
            max_len = max(max_len, i-start_idx+1)
            last_idx[s[i]]=i
        return max_len