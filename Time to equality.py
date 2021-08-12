class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        val = 0
        ans = 0
        for i in range(0,n):
            val = max(val,A[i])
        for i in range(0,n):
            ans = ans + val - A[i]
        return ans