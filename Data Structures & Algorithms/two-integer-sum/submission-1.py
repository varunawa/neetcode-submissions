class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # send in a list and a target where elements in the list must equal the target. return index pos
        # sort list from descending to ascending then subtract 

        matches = {}
        for i, num in enumerate(nums):
            goal = target - num
            
            if goal in matches:
                return [matches[goal], i]
            else:
                matches[num] = i

        return []