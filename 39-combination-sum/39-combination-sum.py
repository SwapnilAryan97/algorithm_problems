class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        table = [[]]*(target+1)
        table[0] = [[]]
        i=0
        candidates.sort()
        while i<=target:
            for num in candidates:
                if i+num<=target:
                    temp = deepcopy(table[i])
                    for j in range(len(temp)):
                        temp[j].append(num)
                        temp[j].sort()
                    if len(table[i+num])==0:
                        table[i+num] = temp
                    else:
                        for val in temp:
                            if val in table[i+num]:
                                continue
                            else:
                                table[i+num].append(val)
                        # table[i+num].sort()
                else:
                    break
            i+=1

        return table[target]