class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        n = len(A)
        for i in range(1,n):
            c = A[i]
            if(not(c >= 'A' and c <= 'Z') and not(c >= 'a' and c <= 'z')):
                 return 0
        return 1


class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for x in A:
            if(x.isalpha() == 0):
                return 0
        return 1