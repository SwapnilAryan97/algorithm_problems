class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op_dict = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}
        return sum(op_dict[op] for op in operations)
        
        
#         res = 0
#         for str in operations:
#             if str[0]=='X':
#                 if str[1]=='-':
#                     res -=1
#                 if str[1]=='+':
#                     res +=1
            
#             elif str[0]=='-':
#                 res -=1
#             else:
#                 res +=1
#         return res