# # Bubble sort
# nums = [1,2,3,4,5,6,7,9,8]
# n = len(nums)
# print(f"len is {n}")
# for i in range(n):
#     print(f"i is {i}")
#     isSwap = False
#     for j in range (n-i-1):
#         print(f"j is {j}")
#         if nums[j] > nums[j+1]:
#             # swap the values
#             temp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = temp
#             isSwap = True
#         if not isSwap:
#             break
# print(nums)

# ==========================================================================

# # Insertion sort 

# nums = [2,3,5,1,9,6,8,7]
# n = len(nums)

# for i in range (1,n):
#     key= nums[i]
#     # print(f"key is {key}")
#     j=i-1
#     # numsJ=nums[j]
#     # print(f"j is {numsJ}")
#     while j>=0 and nums[j]>key:
#         nums[j+1] = nums[j]
#         j-=1
#         nums[j+1] = key
# print(nums)


# =======================================================================

# # selection sort

# nums = [2,3,5,1,9,6,8,7]
# n = len(nums)
# for i in range (n):
#     mn = nums[i]
#     ind = i
#     for j in range(i+1,n):
#         if nums[j] < mn:
#             mn = nums[j]
#             ind = j
    
#     temp = nums[i]
#     nums[i] = nums[ind]
#     nums[ind]= temp

# print(nums)


# =======================================================

# Merge sort 
