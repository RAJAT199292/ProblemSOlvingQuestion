class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for x in A:
            if(x.isnualpha() == 0):
                return 0
        return 1