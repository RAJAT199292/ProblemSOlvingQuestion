class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A)):
                if(i == j):
                    continue
                if A[i] + A[j] == B:
                    return 1
        else:
            return 0