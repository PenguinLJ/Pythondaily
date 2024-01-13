"""
在《英雄联盟》的世界中，有一个叫“提莫”的英雄。
他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
当提莫攻击艾希，艾希的中毒状态正好持续duration秒。
正式地讲，提莫在t发起攻击意味着艾希在时间区间[t，t+duration-1]（含t和t+duration-1）处于中毒状态。
如果提莫在中毒影响结束前再次攻击，中毒状态计时器将会重置，在新的攻击之后，中毒影响将会在duration秒后结束。
给你一个非递减的整数数组timeSeries，其中timeSeries[i]表示提莫在timeSeries[i]秒时对艾希发起攻击，
以及一个表示中毒持续时间的整数duration。
返回艾希处于中毒状态的总秒数。
"""
timeSeries1 = [2, 3, 4]
timeSeries2 = [1, 4]
timeSeries3 = [1, 2]
duration = 2


# 错误
# def totalpoisontime(timeSeries, duration):
#     if len(timeSeries) == 0:
#         return 0
#     elif len(timeSeries) == 1:
#         return timeSeries[0] + duration - timeSeries + 1
#     else:
#         start_posion = timeSeries[0]
#         end_poison = timeSeries[-1] + duration - 1
#         return (end_poison - start_posion) * duration
#
#
# print(totalpoisontime(timeSeries1, duration))
# print(totalpoisontime(timeSeries2, duration))
# print(totalpoisontime(timeSeries3, duration))

##GPT写法
def total_poison_duration(timeSeries, duration):
    if not timeSeries:  # 特殊情况处理： 如果timeSeries为空，说明没有攻击，直接返回中毒总时间为0。
        return 0

    total_duration = 0  # 初始化中毒总时间： 使用total_duration变量来记录中毒的总时间。

    for i in range(1, len(timeSeries)):  # 遍历攻击时间点数组： 使用for循环遍历timeSeries数组。
        gap = timeSeries[i] - timeSeries[i - 1]  # 计算攻击时间间隔： 计算当前攻击和前一次攻击之间的时间间隔。
        total_duration += min(gap, duration)  # 累加中毒时间： 将当前时间间隔与duration中取较小值，表示本次攻击的中毒时间，将其累加到总中毒时间上。

    return total_duration + duration  # 最后一个攻击的中毒时间


# 示例用法

print(total_poison_duration(timeSeries2, duration))  # 输出: 4

print(total_poison_duration(timeSeries3, duration))  # 输出: 3


