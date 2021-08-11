class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        state = 0
        ans = 0

        for i in range(0, len(A)):
            if (A[i] == state):
                ans += 1
                state = 1 - state
        return ans