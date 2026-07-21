class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = [];
        
        # as soon as it finds a duplicate, return false 
        for num in nums:
            if num in seen:
                return True
            
            seen.append(num)

        return False
