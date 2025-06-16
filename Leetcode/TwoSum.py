nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is found in the map, return the solution
            if complement in complement_map:
                return [complement_map[complement], i]
            
            # Store the current number's index as a potential complement for future numbers
            complement_map[num] = i
            
        # Return an empty list if no solution is found
        # This line is optional depending on if you want to signal no solution explicitly
        return []