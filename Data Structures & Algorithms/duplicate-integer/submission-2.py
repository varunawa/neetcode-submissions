class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_arr = []

        for num in nums:
            if num not in num_arr:
                num_arr.append(num)
            else:
                return True

        return False