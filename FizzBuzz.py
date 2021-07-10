# FizzBuzz
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        lst = []
        for i in range(1,A+1):
            if i % 5 == 0:
                if i % 3 == 0:
                    lst.append('FizzBuzz')
                else:
                    lst.append('Buzz')
            elif i % 3 == 0:
                lst.append('Fizz')
                continue
            else:
                lst.append(i)
        return lst