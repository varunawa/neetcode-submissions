class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers: non-decreasing
        # using pointer1, find what pointer should be using target and look through rest of array
        p1 = 0
        while p1 < len(numbers):
            index2_val = target - numbers[p1]
            p2 = p1 + 1
            while (p2) < len(numbers):
                if numbers[p2] == index2_val:
                    return [p1+1, p2+1]
                p2 += 1

            p1 += 1
        
        return 