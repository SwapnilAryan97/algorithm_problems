class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        temp = ""
        flag = True
        for i in range(len(num)):
            if flag and num[i]=='6':
                flag = False
                temp+='9'
                continue
            temp+=num[i]
        return temp