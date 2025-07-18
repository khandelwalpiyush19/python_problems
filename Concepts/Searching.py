# binary search 

# nums = [2,6,8,3,1,4,5]
# key = 6
# n = len(nums)
# nums.sort()
# print(nums)
# l = 0
# r = n
# index = 0
# for i in range(n):
#     mid = (l+r)//2
#     if nums[mid] == key:
#         index = mid
#     elif nums[mid] > key :
#         r = mid -1
#     elif nums[mid] < key :
#         l = mid+1

# print(index)


# nums = [2, 6, 8, 3, 1, 4, 5]
# key = 6

# nums.sort()
# print("Sorted array:", nums)

# l = 0
# r = len(nums) - 1
# index = -1  # Default to -1 if not found

# while l <= r:
#     mid = (l + r) // 2
#     if nums[mid] == key:
#         index = mid
#         break
#     elif nums[mid] > key:
#         r = mid - 1
#     else:
#         l = mid + 1

# print("Index of key:", index)

# ====================================LOWER BOUND===========================================

# nums = [2, 6, 8, 3, 1, 4, 5]
# key = 7

# n= len(nums)
# nums.sort()
# print("Sorted array:", nums)

# l = 0
# r = n - 1
# index = n # Default to -1 if not found

# while l<=r:
#     mid = l + (r-l)//2
#     if nums[mid]>=key:
#         index=mid
#         r=mid-1
#     else:
#         l=mid+1

# print(index)
# ====================================UPPER BOUND===========================================

# nums = [2, 6, 8, 3, 1, 4, 5]
# key = 7

# n= len(nums)
# nums.sort()
# print("Sorted array:", nums)

# l = 0
# r = n - 1
# index = n # Default to -1 if not found

# while l<=r:
#     mid = l + (r-l)//2
#     # just remove "=" and get the code for upper bound .
#     if nums[mid]>key:
#         index=mid
#         r=mid-1
#     else:
#         l=mid+1

# print(index)

# ==========================================Floor and ceil===============================
nums = [2, 6, 8, 3, 1, 4, 5,9]
key = 7

n= len(nums)
nums.sort()
print("Sorted array:", nums)

l = 0
r = n - 1
index = n # Default to -1 if not found

while l<=r:
    mid = l + (r-l)//2
    if nums[mid]>=key:
        index=mid
        r=mid-1
    else:
        l=mid+1

print(f"floor is {nums[index-1]}")
print(f"ceil is {nums[index]}")