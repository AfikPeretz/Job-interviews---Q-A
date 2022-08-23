# o(nlogn) solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()     # o(nlogn)
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]
        for i in range(1, len(nums) - 2):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]
        return 0
    


# o(n) solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        emptyDict = {}
        for num in nums:
            key = num
            if key in emptyDict.keys():
                emptyDict[num] = num
            else:
                emptyDict[num] = None
        for key in emptyDict:
            if emptyDict[key] == None:
                return key
        return 0
