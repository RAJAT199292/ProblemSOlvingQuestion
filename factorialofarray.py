# Groot has an array A of size N. Boring right? Groot thought so too, so he decided to construct another array B of the same size and defined elements of B as:
# B[i] = factorial of A[i] for every i such that 1<= i <= N.
# factorial of a number X denotes (1 x 2 x 3 x 4......(X-1) x (X)).
# Now Groot is interested in the total number of non-empty subsequences of array B such that every element in the subsequence has the same non empty set of prime factors.
# Since the number can be very large, return it modulo 109 + 7.
# NOTE: A set is a data structure having only distinct elements. Eg : the set of prime factors of Y=12 will be {2,3} and not {2,2,3}

maxN = 1000001
prime = [0] * maxN
flag = 0
mod = 1e9 + 7

def pre():
    global flag, maxN, prime
    flag = 1
    prime[1] = 1
    for i in range(2, maxN):
        if(prime[i] == 0):
            j = i * i
            while(j < maxN):
                prime[j] = 1
                j += i
def power(x, y):
    res = 1
    while(y):
        if(y % 2):
            res = (x * res) % mod
        y = y // 2
        x = (x * x) % mod
    return res

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        global flag, prime,mod
        if(flag == 0):
            pre();
        n = len(A)
        A.sort()
        v = []
        for i in range(2, A[n - 1] + 1):
            if(prime[i] == 0):
                v.append(i)
        ans = 0
        j = 0 
        i = 0
        while(i < n and j < len(v)):
            cnt = 0
            if(A[i] == 1):
                i += 1
                continue
            while(i < n and A[i] < v[j]):
                i += 1
                cnt += 1
            temp = power(2, cnt) - 1
            temp += mod
            temp %= mod
            ans += temp
            ans %= mod
            j+=1
        if(i < n):
            temp = power(2, n - i) -1
            temp += mod
            temp %= mod
            ans += temp
            ans %= mod
        return int(ans)