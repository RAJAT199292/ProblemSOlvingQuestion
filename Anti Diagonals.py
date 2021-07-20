class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        p = len(A[0])
	    res = [0]*(2*p-1)
	    for i in range((2*p)-1):
	        res[i] = []
	    for i in range(p):
	        for j in range(p):
	            res[i+j].append(A[i][j])
	    for i in range(2*p-1):
	        while len(res[i]) < p:
	            res[i].append(0)
	    return res