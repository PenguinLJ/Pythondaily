"""
小镇里有n个人，按从1到n的顺序编号。传言称，
这些人中有一个暗地里是小镇法官。如果小镇法官真的存在，那么：
1.小镇法官不会信任任何人。2.每个人（（除了小镇法官）都信任这位小镇法官。
只有一个人同时满足属性1和属性2。
给你一个数组trust，其中trust[i]=[ai，bi]表示编号为ai的人信任编号为bi的人。
如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回-1。

输入：n=2,trust=[[1,2]]
输出：2

输入：n=3，trust=[[1,3],[2,3]]
输出：3

输入：n=3,trust=[[1,3],[2,3],[3,1]]
输出：-1

输入：n=4,trust=[[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
"""


# gpt's answer
def find_judge(n, trust):
    # 初始化每个人的入度和出度
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    # 统计每个人的入度和出度
    for t in trust:
        out_degree[t[0]] += 1
        in_degree[t[1]] += 1

    # 查找法官
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i

    return -1


# 测试例子
print(find_judge(2, [[1, 2]]))  # 输出: 2
print(find_judge(3, [[1, 3], [2, 3]]))  # 输出: 3
print(find_judge(3, [[1, 3], [2, 3], [3, 1]]))  # 输出: -1
print(find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 输出: 3
