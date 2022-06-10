class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # print(list(sentences[0]))
        # print(sentences[0].strip(" ")[])
        x=0
        res = 0
        for i in range(len(sentences)): 
            x+=sentences[i].strip().count(" ")
            res = max(x+1,res)
            x=0
        return res
        