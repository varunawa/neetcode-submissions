class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # go through all items, storing them in 
        # seen = []

        # for num in nums:
        #     if num in seen:
        #         return True
            
        #     seen.append(num)
        
        # return False

        return len(nums) != len(set(nums))
