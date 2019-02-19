class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        map = {}
        for x in range(len(nums)):
            if nums[x] not in map:
                map[target-nums[x]] = x 
            else:
                return map[nums[x]], x
