class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] > nums[k] and
                    nums[i] + nums[k] > nums[j] and
                    nums[k] + nums[j] > nums[i]):
                        count +=1
        return count


# best solution with n2 complex

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(0, n-2):
            k = i + 2
            for j in range(i + 1, n):
                while(k < n and nums[i] + nums[j] > nums[k]):
                    k +=1
                if(k>j):
                    count += k - j - 1
        return count