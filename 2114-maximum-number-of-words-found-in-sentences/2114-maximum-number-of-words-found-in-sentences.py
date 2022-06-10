class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # x=0
        # res = 0
        # for i in range(len(sentences)): 
        #     x+=sentences[i].strip().count(" ")
        #     res = max(x+1,res)
        #     x=0
        # return res
    
        "Another solution"
        res = 0
        for x in sentences:
            if len(x.split(' '))>res:
                res = len(x.split(' '))
        return res

        
    
    
        