"""
给你一个数组candies和一个整数extraCandies，其中candies[i]代表第i个孩子拥有的糖果数目。
对每一个孩子，检查是否存在一种方案，将额外的extraCandies个糖果分配给孩子们之后，此孩子有最多的糖果。
注意，允许有多个孩子同时拥有最多的糖果数目。
示例：输入:candies =[4,2,1,1,2],extraCandies=1
输出：[true,false,false,false,false]
解释：只有1个额外糖果，所以不管额外糖果给谁，只有孩子1可以成为拥有糖果最多的孩子。
输入：candies=[12,1,12],extraCandies=10
输出：[true,false,true]
输入：candies =[2,3,5,1,3],extraCandies =3
输出：[true,true,true,false,true]
"""

candies1 = [4, 2, 1, 1, 2]
extraCandies1 = 1
candies2 = [12, 1, 12]
extraCandies2 = 10
candies3 = [2, 3, 5, 1, 3]
extraCandies3 = 3


def themostcandy(candies, extraCandies):
    max_candy = max(candies)  # 最大糖果的数量
    num_children = len(candies)  # 孩子的数量
    out = [False] * num_children
    for i in range(num_children):
        if (candies[i] + extraCandies) >= max_candy:
            out[i] = True

    print(out)


themostcandy(candies1, extraCandies1)
themostcandy(candies2, extraCandies2)
themostcandy(candies3, extraCandies3)

# 做出来了，舒服

# 以下是老师的答案
# candies = [4, 2, 1, 1, 2]
# extraCandies = 1
# ls = [candy + extraCandies >= max(candies) for candy in candies]
# print(ls)
