
# Explanation 2:
#  There is no subset that add up to 30.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        visited=0
        if visited == 0 and sum(A) < B:
            return 0
        if visited >= len(A):
            return 0
        if B == 0 or B in A:
            return 1
        if A[visited] <= B:
            if self.solve(A, B - A[visited], visited + 1):
                return 1
        without = self.solve(A, B, visited + 1)
        if without:
            return 1
        return 0
    