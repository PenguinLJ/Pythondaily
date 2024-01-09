"""
有一堆石头，每块石头的重量都是正整数。每一回合，从中选出两块最重的石头，
然后将它们一起粉碎。假设石头的重量分别为×和y，且×<=y。那么粉碎的可能结果如下：
如果x==y，那么两块石头都会被完全粉碎；
如果x！=y，那么重量为×的石头将会完全粉碎，而重量为y的石头新重量为y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回0。
输入：[2,7,4,1,8,1]输出：1
解释：先选出7和8，得到1，所以数组转换为[2，4，1，1，1]，
再选出2和4，得到2，所以数组转换为[2，1，1，1]，
接着是2和1，得到1，所以数组转换为[1，1,1]，
最后选出1和1，得到0，最终数组转换为[1]，
这就是最后剩下那块石头的重量。
"""

stones = [2, 7, 4, 1, 8, 1]

# def crushedstone(stones):  # 使用排序
#     while len(stones) > 1:
#         stones.sort(reverse=True)
#         weightest = stones[0]
#         secondweighest = stones[1]
#         if weightest == secondweighest:
#             stones.remove(weightest)
#             stones.remove(secondweighest)
#         else:
#             gravel = weightest - secondweighest
#             stones.remove(weightest)
#             stones.remove(secondweighest)
#             stones.append(gravel)
#
#     if len(stones) == 1:
#         return stones[0]
#     else:
#         return 0

# def crushedstone2(stones):  # 不使用排序
#     while len(stones) > 1:
#         weightest = max(stones)
#         stones.remove(weightest)
#         secondweighest = max(stones)
#         if weightest == secondweighest:
#             stones.remove(secondweighest)
#         else:
#             gravel = weightest - secondweighest
#             stones.remove(secondweighest)
#             stones.append(gravel)
#             print(stones)
#
#     if len(stones) == 1:
#         return stones[0]
#     else:
#         return 0
#
#
# print(crushedstone2(stones))


## up主写法
st = sorted(stones)
while len(st) > 1:
    if st[-1] - st[-2] == 0:
        st = st[:-2]
    else:
        st = sorted(st[:-2] + [st[-1] - st[-2]])
if st is None:
    print("石头全部被粉碎")
else:
    print(f"剩下的一块石头重量为 {st[0]}")


'''  # chatgpt的解法
def crushedstone(stones):
    while len(stones) > 1:
        stones.sort(reverse=True)
        weightest = stones[0]
        secondweighest = stones[1]
        if weightest == secondweighest:
            stones = stones[2:]
        else:
            gravel = weightest - secondweighest
            stones = stones[2:]
            stones.append(gravel)

    if len(stones) == 1:
        return stones[0]
    else:
        return 0

print(crushedstone(stones))'''
