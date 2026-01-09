class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
            return index
        except ValueError:
            return -1


# other solution
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        nums_tuple = [(value, index) for index, value in enumerate(nums)]
        nums_tuple.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = nums_tuple[mid][0]

            if target == mid_value:
                return nums_tuple[mid][1]

            elif mid_value < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
