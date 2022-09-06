#with dict
def majorityElement(nums):
    newdict = {}
    for i in range (0, len(nums)):
        if newdict.get(nums[i]) == None:
            newdict.update({nums[i]: 1})
        else:
            counter = newdict[nums[i]] + 1
            newdict.update({nums[i] : counter})
    return max(newdict, key=newdict.get)
    
    
    
    
#with array (more faster)
def majorityElement(nums):
        array = [0] * (max(nums) + 1)
        for i in nums:
            array[i] += 1
        return array.index(max(array))