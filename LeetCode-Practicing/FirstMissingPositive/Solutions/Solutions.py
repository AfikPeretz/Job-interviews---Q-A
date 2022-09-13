def firstMissingPositive(nums):
    maxFromNums = max(nums)
    if maxFromNums> 100000: #edge case
        array = [0] * (100000)
    elif maxFromNums<1: #edge case
        return 1
    else:
        array = [0] * (maxFromNums+1)
    array[0] = 1
    for i in range (0, len(nums)):
        if nums[i] > 0 and nums[i] < len(array):
            array[nums[i]] = 1
    for i in range (0, len(array)):
        if array[i] != 1:
            return i
    return (maxFromNums + 1)