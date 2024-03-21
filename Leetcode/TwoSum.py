nums = [2,7,11,15]
target = 9

def twoSum(self, nums: List[int], target: int) -> List[int]:
         listr=[]
         i=0
        for x in nums:
            y = x - target
            if y == x[i+1]:
                x1=x[i]
                x2=x[i+1]
                listr.apend(x1)
                listr.apend(x2)
            else: i += 1
        return listr