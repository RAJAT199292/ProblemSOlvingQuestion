class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        lo = 0
        hi = len(A)-1
        mid = 0
        while(mid <= hi):
            if A[mid] == 0:
                A[lo], A[mid] = A[mid],A[lo]
                lo = lo+1
                mid = mid +1
            elif A[mid] == 1:
                mid = mid +1
            else:
                A[mid],A[hi] = A[hi],A[mid]
                hi = hi -1
        return A