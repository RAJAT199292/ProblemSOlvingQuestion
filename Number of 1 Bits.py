class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        temp = 0
        while A != 0:
            temp = temp + 1
            A = A & (A-1)
        return temp