class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mem = {}
        for word in strs:
            sortword = ''.join(sorted(word))
            if sortword not in mem:
                mem[sortword] = [word]
            else:
                mem[sortword].append(word)
        
        for val in mem.values():
            res.append(val)
        return res
        
        
        
#         res = []
#         temp = []
        
#         def helper(arr):
#             if not arr:
#                 return
            
#             word = arr[0]
#             temp.append(word)
            
#             for i in range(1,len(arr)):
#                 if collections.Counter(word)==collections.Counter(arr[i]):
#                     temp.append(arr[i])
#             return
        
        
#         while strs:
#             if len(strs)==1:
#                 res.append([strs[0]])
#                 break

#             helper(strs)
#             res.append(temp)
#             for word in temp:
#                 strs.remove(word)
#             temp = []
            
#         return res
            
            