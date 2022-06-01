# T.C. O(V+E) - number of elements in trust
# S.C. O(V) - V number of person
class Solution:
    
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg=[0 for _ in range(n)]

        for a,b in trust:
            indeg[a-1]-=1
            indeg[b-1]+=1
        # print(indeg)
        for i in range(len(indeg)):
            if indeg[i]==n-1:
                return i+1
        return -1
