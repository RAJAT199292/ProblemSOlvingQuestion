class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        ans1, ans2 = 0, 0
        x, y = 1, 0
        
        for it in A:
            it=(it&1)
            if(it==x):
                ans1+=1
                x^=1
                
            if(it==y):
                y^=1;
                ans2+=1
        
        return max(ans1,ans2)