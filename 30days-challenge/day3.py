# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # solve by kadane's algorithm (O(n))

        max_so_far = max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            max_ending_here = max(max_ending_here, nums[i])
            max_so_far = max(max_so_far, max_ending_here)
#             if current_end <= 0:
#                 current_start=current_end
#                 current_sum = i
#                 print(current_sum)
#             else:
#                 current_sum += i
#                 print(current_sum)

#             if current_sum > best_sum:
#                 best_sum = current_sum
#                 best_start = current_start
#                 best_end = current_end + 1
        return max_so_far
        #     current_sum = max(0, current_sum+i)
        #     best_sum = max(best_sum, current_sum)
        # return best_sum
