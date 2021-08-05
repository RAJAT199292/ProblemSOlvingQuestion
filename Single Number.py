class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(Self, A):
        temp = A[0]
        for i in range(1,len(A)):
            temp = temp ^ A[i]
        return temp