"""
给你一个整数数组且nums，请你选择数组的两个不同下标i和j，
使（nums[i]-1)*（nums[j]-1）取得最大值。请你计算并返回该式的最大值。
输入：nums=[3，4,5,2]
输出：12
解释：如果选择下标i=1和j=2（下标从0开始），则可以获得最大值，（nums[1]-1）*（nums[2]-1）=（4-1)*（5-1)=3*4=12。

输入：nums=[1,5,4,5]
输出：16
解释：选择下标i=1和j=3（下标从0开始），则可以获得最大值（5-1）*（5-1）=16。

输入：nums=[3,7]
输出：12
"""

nums = [3, 4, 5, 2]


# def maxmiumproduct(numbers):
#     biggest = max(numbers)
#     numbers.remove(biggest)
#     secondbiggest = max(numbers)
#     return (biggest - 1) * (secondbiggest - 1)
#
#
# print(maxmiumproduct(nums))

def maxmiumproduct(numbers):  # gpt
    if len(numbers) < 2:
        return None  # 处理数组长度小于2的情况

    sorted_nums = sorted(numbers, reverse=True)
    return (sorted_nums[0] - 1) * (sorted_nums[1] - 1)


print(maxmiumproduct(nums))
