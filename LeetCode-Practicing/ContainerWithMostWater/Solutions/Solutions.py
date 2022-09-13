#O(n^2) - naive solution

def maxArea(height):
    max = 0
    for i in range (0, len(height)):
        for j in range (0, len(height)):
            mini = min(height[i], height[j])
            if max < (mini * abs(j-i)):
                max = (mini * abs(j-i))
    return max
    
#O(n) 

def maxArea(height):
    res = 0
    i = 0
    j = len(height) - 1
    while i < j:
        container = (j - i) * min(height[j], height[i])
        res = max(res, container)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res