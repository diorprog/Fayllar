#1

# def twoSum(nums, target):
#
#     complement_dict = {}
#
#     for i, num in enumerate(nums):
#         complement = target - num
#
#         if complement in complement_dict:
#             return [complement_dict[complement], i]
#
#         complement_dict[num] = i
#
#     return []
#
# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))


#2


# def removeDuplicates(nums):
#     if len(nums) == 0:
#         return 0
#
#     k = 1
#
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[k] = nums[i]
#             k += 1
#
#     return k


#3


# def remove_elements(nums, val):
#     while val in nums:
#         nums.remove(val)
#     return len(nums)
#
# nums = [3, 2, 2, 3, 2, 4, 5, 6, 2]
# val = 3
#
# k = remove_elements(nums, val)
# print(k)
# print(nums)


#4


# def searc(nums, target):
#     l, h = 0, len(nums) - 1
#
#     while l <= h:
#         m = (l + h) // 2
#         if nums[m] == target:
#             return m
#         elif nums[m] < target:
#             l = m + 1
#         else:
#             h = m - 1
#
#     return l
#
# nums = [1, 3, 5, 6]
# target = 4
# index = searc(nums, target)
# print(index)


#5

#
# def pl(d):
#     n = len(d)
#
#     for i in range(n - 1, -1, -1):
#         if d[i] < 9:
#             d[i] += 1
#             return d
#
#         d[i] = 0
#
#     d.insert(0, 1)
#     return d
#
# d = [1, 2, 9]
# res = pl(d)
# print(res)



#6



# def merge(nums1, m, nums2, n):
#     index1 = m - 1
#     index2 = n - 1
#     index3 = m + n - 1
#
#     while index1 >= 0 and index2 >= 0:
#         if nums1[index1] > nums2[index2]:
#             nums1[index3] = nums1[index1]
#             index1 -= 1
#         else:
#             nums1[index3] = nums2[index2]
#             index2 -= 1
#         index3 -= 1
#
#     while index2 >= 0:
#         nums1[index3] = nums2[index2]
#         index2 -= 1
#         index3 -= 1
#
#
# nums1 = [1, 3, 5, 0, 0, 0]
# nums2 = [2, 4, 6]
# m = 3
# n = 3
#
# merge(nums1, m, nums2, n)


#7


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def sortedArrayToBST(nums):
#     if not nums:
#         return None
#
#     m = len(nums) // 2
#
#     r = TreeNode(nums[m])
#
#     r.leftl = sortedArrayToBST(nums[:m])
#     r.right = sortedArrayToBST(nums[m + 1:])
#
#     return r
#
#
# nums = [-10, -3, 0, 5, 9]
# r = sortedArrayToBST(nums)



#8



# def generate_pascals_triangle(num):
#     t = []
#     for i in range(num):
#         r = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 r.append(1)
#             else:
#                 r.append(t[i - 1][j - 1] + t[i - 1][j])
#         t.append(r)
#     return t
#
# num = 5
# result = generate_pascals_triangle(num)
# for r in result:
#     print(r)



#9



# def get_pascal_triangle_row(rowindex):
#     row = [1]
#
#     for i in range(rowindex):
#         new_row = [1]
#
#         for j in range(1, len(row)):
#             new_row.append(row[j-1] + row[j])
#
#         new_row.append(1)
#         row = new_row
#
#     return row
#
# rowindex = 5
# triangle_row = get_pascal_triangle_row(rowindex)
# print(triangle_row)


#10


# def maxProfit(prices):
#     if len(prices) < 2:
#         return 0
#
#     min_price = prices[0]
#     max_profit = 0
#
#     for i in range(1, len(prices)):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         else:
#             max_profit = max(max_profit, prices[i] - min_price)
#
#     return max_profit
#
#
# prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))