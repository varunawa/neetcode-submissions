import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []

        for i in range(len(nums)):
            temp_arr = nums[:i] + nums[i+1:]
            p = math.prod(temp_arr)
            
            prod.append(p)
        
        return prod

