# # Bubble sort
# nums = [1,2,3,4,5,6,7,9,8]
# n = len(nums)
# print(f"len is {n}")
# for i in range(n):
#     print(f"i is {i}")
#     isSwap = False
#     for j in range(n-i-1):
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


# strs = ["flower", "flow", "flight"]
# x = sorted(strs)
# print(x)

# # Start with the first string as reference
# first = x[0]
# last = x[-1]
# prefix = ""

# # Compare characters of first and last string
# for i in range(min(len(first), len(last))):
#     if first[i] == last[i]:
#         prefix += first[i]
#     else:
#         break

# print("Longest common prefix:", prefix)
# =======================================================================

# s = "abcde"
# goal = "cdeab"
# rotated = ""
# for i in range(len(s)):
#     rotated = s[i:] + s[:i]
#     if rotated == goal:
#         print(True)
#         break
# # rotated = s[1:] + s[0]
# # rotated_1 = rotated[1:] + rotated[0]
# # print(rotated)
# # print(rotated_1)



# ==================================================================================================================

# nums1 = [1,3,5]
# nums2 = [2,4]
# nums1.extend(nums2)
# nums1.sort()
# print(nums1)
# median = 0
# n= len(nums1)
# if n%2 == 0:
#     i = n//2
#     median= (nums1[i] + nums1[i-1]) / 2
# else :
#     i = (n//2)
#     print(f"i is is {i}")
#     median = nums1[i]
# print(median)

# =======================================================================================

# s = "eguhugchmtcmtumtumummcmvkxoapzjnxifioxzuam"

# # Step 1: Frequency dictionary
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)

# # Step 2: Sort characters by frequency
# sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# print(sorted_chars)

# # Step 3: Rebuild string based on sorted frequencies
# sorted_str = "".join(ch * freq for ch, freq in sorted_chars)

# print(sorted_str)

# ======================================================================================

# import re


# s= "-0232432ssd"
# digits = re.sub(r"\D", "", s)
# print(digits)
# for ch in digits:
#     if digits[0] == '-':
#         digits= -digits
# cleaned = digits.lstrip("0")
# print(cleaned)

# ==========================================================================================

# s = "baba"
# ss_list = []
# n = len(s)
# for i in range(n):
#     for j in range(i,n):
#         ss = s[i:j+1]
#         ss_list.append(ss)
# sss_list = sorted(ss_list)
# # sss_list = list(set(sss_list))
# lss =sss_list.count(sss_list)
# print(lss)
# ========================================================================================================================

# s = "()(())((()()))"
# count = 0
# max_val = 0

# for i in range(len(s)):
#     if s[i] == '(':
#         count += 1
#         max_val = max(max_val, count)
#     elif s[i] == ')':
#         count -= 1

# print(max_val)
# ====================================================================================================
# s="Hello*"
# a=0
# b=0
# for i in s:
#     if i=='*':
#         a+=1
#     elif i=='#':
#         b+=1
# print(a-b)
# ==========================================================================================================
# size = int(input("Enter the size of the list: "))
# my_list = []
# max_val = 0
# count= 1
# for i in range(size):
#     value = input(f"Enter unique value {i+1}: ")
#     my_list.append(value)

# print("Generated list:", my_list)

# for i in range(size):
#     max_val = max(my_list[i],my_list[i-1])
#     if max_val == my_list[i]:
#         count+=1
    
# print(count)

# ===========================================================================================================
# e = [7,0,5,1,3] 
# l = [1,2,1,3,4]
# max_g = 0
# for i1,i2 in zip(e,l):
#     val = i1-i2
#     guest = val

