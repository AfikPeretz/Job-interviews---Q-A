#O(m + n)
def merge(nums1, m, nums2, n):
    if n == 0:
        nums1
    else:
        i,j,k = 0,0,0
        nums3 = ['']*(m+n)
        for v in range (m, m+n):
            nums1[v] = pow(10,9)
        while (k != m+n):
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums3[k] = nums2[j]
                k += 1
                nums2[j] = pow(10,9)
                if j != len(nums2)-1:
                    j += 1      
        for q in range (0,m+n):
            nums1[q] = nums3[q]