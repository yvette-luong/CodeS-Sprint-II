
# High Similarity Solutions
'''
def findValueSortedShiftedArray(nums, target):
    if not nums:
        return -1
    
    min_num, max_num = 0, len(nums) - 1
    
    while min_num <= max_num:
        mid_num = (min_num + max_num) // 2
        if target == nums[mid_num]:
            return mid_num
            
        if nums[min_num] <= nums[mid_num]:
            if nums[min_num] <= target <= nums[mid_num]:
                max_num = mid_num - 1
            else:
                min_num = mid_num + 1
        else:
            if nums[mid_num] <= target <= nums[max_num]:
                min_num = mid_num + 1
            else:
                max_num = mid_num - 1
    
    return -1
    
'''

def findValueSortedShiftedArray(nums, target):
    if not nums:
        return -1

    low, high = 0 , len(nums) - 1

    while low <= high:
        mid = (low + high)//2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else: 
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
