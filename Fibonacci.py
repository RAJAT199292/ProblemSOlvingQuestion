class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        
        if A < 0:
            return False
        elif A == 0:
            return 0
        elif A == 1:
            
            return 1
        else:
            return self.findAthFibonacci(A-1)+self.findAthFibonacci(A-2)