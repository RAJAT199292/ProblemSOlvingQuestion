# Greatest Common Divisor
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while(B != 0):
            r = A%B
            A=B
            B=r
        return A

# second sou;ation
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):
        if (b == 0):
		    return a
        else:
		    return self.gcd(b, a%b)