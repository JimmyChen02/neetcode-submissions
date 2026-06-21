class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_arr = [1] * len(nums)

        before = 1
        for i, num in enumerate(nums):
            return_arr[i]= before
            before *= num
        after = 1
        for i in range(len(nums)-1, -1, -1):
            return_arr[i] *= after
            after *= nums[i]
        return return_arr



        # [1,0,3]
        # before = [1,1,0]
        # after = [0,3,0]