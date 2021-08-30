# Two Sum
# /**
#  * @param {number[]} nums
#  * @param {number} target
#  * @return {number[]}
#  */
# var twoSum = function (nums, target) {
# var len = nums.length;
# for (var i = 0; i < len; i++) {
#     for (var j = i + 1; j < len; j++) {
#         if (nums[i] + nums[j] == target) {
#             return [i,j];
#         }
#     }
#   }
# };


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                n = len(nums)
                for i in range(n):
                    for j in range(i+1,n):
                        if(nums[i] + nums[j] == target):
                            return [i,j]