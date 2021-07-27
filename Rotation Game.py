def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    
    while T > 0:
        temp = input().split()
        N = int(temp[0])
        A = [0] * N
        for i in range(1, N + 1):
            A[i - 1] = int(temp[i])
        B = int(input())
	    B = B % N
	
    	ans = [0] * (N)
        for i in range(0, N):
        	ans[i] = A[(i-B+N)%N]
        
        for i in range(0, N):
            print(ans[i], end = ' ')
        
        print()
        T -= 1
    return 0

if __name__ == '__main__':
    main()