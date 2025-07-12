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

# nums = [2, 3,1,5,5]
# # s=set(nums)
# # for i in s:
# #     if nums.count(i)>(len(nums)/2):
# #         print(nums.count(i))
# #         print(i)
# new_nums = nums.copy()
# new_nums.sort()
# print(new_nums)
# print(nums[0])


# prices = [2,9 , 1, 3, 4] 
# n= len(prices)
# small = 0
# big = 0
# for i in range(n):
#     print(f"i is {i}")
#     if prices[i] < small:
#         print(f"prices[i] is {prices[i]}")
#         small = prices[i]
#         print(f"small is {small}")
#         for j in range(i+1 , n):
#             if prices[j] > small and prices[j] > big:
#                 big = prices[j]
# print(big - small)

# list1 = [1, 3, 5]
# list2 = ['a', 'b', 'c']

# result = []

# for a, b in zip(list1, list2):
#     result.extend([a, b])

# print(result)

# =======================================leader element===================================================

# nums = [1, 2, 5, 3, 1, 2]
# n = len(nums)
# leader = []

# max_right = float('-inf')
# for i in range(n-1, -1, -1):
#     if nums[i] > max_right:
#         leader.append(nums[i])
#         max_right = nums[i]

# # To match left-to-right order
# leader.reverse()
# print("Leader elements:", leader)

# ==============================================================================================================

# nums = [0,3,7,2,5,8,4,6,0,1]
# sn = nums.copy()
# sn.sort()
# print(sn)
# count = 0
# n = len(sn)
# print(n)
# for i in range(0,n-1):
#     if sn[i+1] == sn[i] + 1:
#         count+=1
# print(count) 

# =========================================================================


# nums = [1,1,1]
# k = 2
# count = 0
# n = len(nums)
# for i in range(n):
#     for j in range(i+1 , n):
#         if k == nums[i] + nums[j]:
#             count +=1
# print(count)
# =======================================================================================

# s = "the sky is blue"
# words = s.split()
# print(words)
# words.reverse()
# print(words)
# joined =' '.join(words)
# print(joined)

# ==========================================================================================

# s = "908975448"
# lo = 0
# for digit in s[::-1]:
#     digit_new = int(digit)
#     if digit_new % 2 != 0:
#         lo=digit_new
#         break
# print(digit_new)

# s="2468246824681246824681"
# nums= [int(char) for char in s]
# n = len(nums)
# li=0
# for i in range(n-1,-1,-1):
#     # print(nums[i])
#     print(i)
#     if nums[i] % 2 != 0:
#         li=i
#         break
# print(s[:li+1])
# # print(lo)
# # print(nums)


strs = ["flower", "flow", "flight"]
x = sorted(strs)
print(x)

# Start with the first string as reference
first = x[0]
last = x[-1]
prefix = ""

# Compare characters of first and last string
for i in range(min(len(first), len(last))):
    if first[i] == last[i]:
        prefix += first[i]
    else:
        break

print("Longest common prefix:", prefix)
   