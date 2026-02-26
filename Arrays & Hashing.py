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

def two_sum(nums, target):
    hash_set = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_set:
            return True
        hash_set[num] = 1
    return False

nums = [3,4,5,6]
target = 7
print(two_sum(nums, target))

# import calendar
# month = calendar.month(1998, 10)
# print(month)
# print(monthcalendar(1998, 10))