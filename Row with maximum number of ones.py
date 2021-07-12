class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        maxCnt = 0
        ansIdx = 0
        for i in range(len(A)):
            cnt = 0
            for j in range(len(A[i])):
                cnt += (A[i][j] == 1)
            if cnt > maxCnt:
                maxCnt = cnt
                ansIdx = i
        return ansIdx