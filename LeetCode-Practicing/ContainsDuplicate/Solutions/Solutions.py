#Just for practice if else in one line
def containsDuplicate1(nums):
    dict = {}
    for i in nums:
        if i not in dict.keys() :
            dict[i] = 1
        else:
            dict[i] += 1
    return True if (max(dict.values())) > 1 else False  


#Sould work faster (not in O() terms but in ϴ())
def containsDuplicate2(nums):
    dict = {}
    for i in nums:
        if i not in dict.keys() :
            dict[i] = 1
        else:
            return True
    return False
