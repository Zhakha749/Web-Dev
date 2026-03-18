def count_evens(nums):
    return sum(1 for x in nums if x % 2 == 0)

def big_diff(nums):
    return max(nums)-min(nums)

def centered_average(nums):
    return (sum(nums)-min(nums)-max(nums))//(len(nums)-2)

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            total += nums[i]
        i += 1
    return total

def sum67(nums):
    total = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True
        elif skip and num == 7:
            skip = False
        elif not skip:
            total += num
    return total

def has22(nums):
    return any(nums[i]==2 and nums[i+1]==2 for i in range(len(nums)-1))