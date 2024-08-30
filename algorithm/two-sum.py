from typing import List
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if dic.get(num) is not None:     
                return [dic.get(num), idx]
            diff = target - num
            dic[diff] = idx
        return []



print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))