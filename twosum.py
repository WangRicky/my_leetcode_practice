class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        sub_index = 0
        operate_list = list(nums)
        operate_list.sort()
        for index, x in enumerate(operate_list):
            if x == target / 2:
                sub_index = index + 1
                break
            elif x > target/2:
                sub_index = index
                break
        front = operate_list[0:sub_index]
        tail = operate_list[sub_index:]
        for x in front:
            temp = target - x
            if temp in tail:
                num1 = x
                num2 = temp
                index1 = nums.index(num1)
                index2 = nums.index(num2)
                if index1 == index2:
                    index2 = nums.index(num2, index1 + 1)
                return [index1, index2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 3], 6))
