
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
# s = "liril"
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
