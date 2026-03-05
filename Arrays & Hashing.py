from calendar import monthcalendar
from unicodedata import lookup

from sympy.physics.optics import lens_formula


# 1. Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Input: nums = [1, 2, 3, 3]
# Output: true

# Input: nums = [1, 2, 3, 4]
# Output: false

# def finding_duplicates(nums):
#     for i in range(len(nums)):
#         # for j in range(1, i): My mistake
#         for j in range(i): # ChatGPT Correction
#             if nums[i] == nums[j]:
#                 return True
#     return False
# arr = [1, 2, 2, 3]
# print(finding_duplicates(arr))

# def finding_duplicate(nums):
#     hash_set = set()
#     for i in range(len(nums)):
#         if nums[i] in hash_set:
#             print(hash_set)
#             return True
#         else:
#             hash_set.add(nums[i])
#             print(hash_set)
#     return False
#
# arr = [1, 2, 3, 4, 4]
# print(finding_duplicate(arr))
# -----------------------------------------------------------------------------------------------------------------------------------------
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Input: s = "racecar", t = "carrace"
# Output: true

# Input: s = "jar", t = "jam"
# Output: false

# def valid_anagram(x, y):
#     if sorted(x) == sorted(y):
#         return True
#     return False
#
# s = "jar"
# t = "jam"
# print(valid_anagram(s, t))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition. Return the answer with the smaller index first.

# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Input: nums = [5,5], target = 10
# Output: [0,1]

# def two_sum(nums, target):
#     hash_set = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hash_set:
#             return hash_set[complement], i
#         hash_set[num] = i
#     return []
#
# nums = [3,4,5,6,7]
# target = 7
# print(two_sum(nums, target))

# import calendar
# month = calendar.month(1998, 10)
# print(month)
# print(monthcalendar(1998, 10))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Input: strs = ["x"]
# Output: [["x"]]
#
# Input: strs = [""]
# Output: [[""]]

# def group_anagram(s):
#     output_list = []
#     x = sorted(s)
#     for i in range(len(x)):
#         for j in range(1, len(x)):
# strs = ["act","pots","tops","cat","stop","hat"]
# print(group_anagram(strs))


import heapq
# def topKFreq(n, k):

    # freq = {}
    # for num in n:
    #     freq[num] = freq.get(num, 0) + 1
    # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # print(f'sorted_freq = {sorted_freq}')
    # result = []
    # for i in range(k):
    #     print(result)
    #     result.append(sorted_freq[i][0])
    # return result

#     freq = {}
#     for num in n:
#         freq[num] = freq.get(num, 0) + 1
#
#     heap = []
#     for key, value in freq.items():
#         heapq.heappush(heap, (value, key))
#         print(f'heap = {heap}')
#         if len(heap) > k:
#             heapq.heappop(heap)
#
#     return [item[1] for item in heap]
#
# nums = [1,2,2,3,3,3]
# k = 2
# print(topKFreq(nums, k))

# def find_product(nums):
    # product_list = []
    # temp = 1
    # for i in range(len(n)):
    #     for j in range(0, len(n)):
    #         print(f'j = {j}, i = {i}')
    #         if j == i:
    #             pass
    #         else:
    #             temp = temp * n[j]
    #     product_list.append(temp)
    #     temp = 1
    # return product_list

    # n = len(nums)
    # result = [1]*n
    # prefix = 1
    # for i in range(n):
    #     result[i] = prefix
    #     prefix *= nums[i]
    #
    # suffix = 1
    # for j in range(n):
    #     result[n] = suffix
    #     suffix *= nums[i]
    # return result

# num = [1, 2, 4, 6]
# print(find_product(num))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4

# def LCS(num):
#     if not num:
#         return 0
#
#     sorted_list = sorted(set(num))
#
#     longest = 1
#     current = 1
#
#     for i in range(len(sorted_list) - 1):
#         if sorted_list[i] + 1 == sorted_list[i+1]:
#             current += 1
#         else:
#             longest = max(longest, current)
#             current = 1
#     return max(longest, current)
#
# nums = [1, 2, 3, 10, 11, 12]
# print(LCS(nums))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Given a string s, return true if it is a palindrome, otherwise return false. A palindrome is a string that reads the same forward and backward.
# It is also case-insensitive and ignores all non-alphanumeric characters.
# Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
#
# Input: s = "Was it a car or a cat I saw?"
# Output: true

# import re
# def isPalindrome(text):
#     ct= re.sub(r"[^a-zA-Z0-9]", "", text).lower()
#     left = 0
#     right = len(ct) - 1
#     while left < right:
#         if ct[left] != ct[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# s = "Was it a car or a cat I saw?"
# print(isPalindrome(s))

# import re
# def isPalindrome(text):
#     ct= re.sub(r"[^a-zA-Z0-9]", "", text).lower()
#     for i in range(len(ct)):
#         left, right = ct[i], ct[len(ct) - 1 - i]
#         if left != right:
#             return False
#     return True
# s = "Was it a car or a cat I saw?"
# print(isPalindrome(s))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Given an array of integers numbers that is sorted in non-decreasing order. Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice. There will always be exactly one valid solution.
#
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]

# def two_sum(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#
#     while left < right:
#         s = numbers[left] + numbers[right]
#         if s == target:
#             return [left + 1, right + 1]
#         elif s < target:
#             left += 1
#         else:
#             right -= 1
#     return []
#
# numbers = [1,2,3,4]
# target = 7
# print(two_sum(numbers, target))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

