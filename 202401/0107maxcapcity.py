"""
给定一个长度为n的整数数组height。有n条垂线，第i条线的两个端点是（i，0）和（i,height[i]).
找出其中的两条线，使得它们与×轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。说明：你不能倾斜容器。
输入：[1,8,6,2,5,4,8,3,7]输出：49
输入：height=[1,1]输出：1
"""

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left, right = 0, len(heights) - 1
max_capcity = 0
L, R = 0, 0

while left != right:
    current_capacity = (right - left) * min(heights[left], heights[right])
    max_capcity = max(max_capcity, current_capacity)
    if current_capacity == max_capcity:
        L, R = left, right
    if left <= right:
        left += 1
    else:
        right -= 1

print(f"The left index is {L},The right index is {R}")
print(f"The max capcity is {max_capcity}.")
