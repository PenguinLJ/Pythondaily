"""
给你一份旅游线路图，该线路图中的旅行线路用数组paths表示，
其中paths[i]=[cityAi,cityBi]表示该线路将会从cityAi直接前往cityBi。
请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。
"""

paths = [['london', 'new york'], ['new york', 'lima'], ['lima', 'sao paulo']]

start = set()  # 创建一个集合用于存放出发城市

for i in paths:  # 遍历路线，将索引0放入集合
    start.add(i[0])
for i in paths:  # 再次遍历路线，
    if i[1] not in start:  # 如果到达城市不在出发集合内，则该城市是最终城市
        print(f"{i[1]} is the end.")

# def find_end_city(paths):
#     start = {path[0] for path in paths}
#     end_city = next(path[1] for path in paths if path[1] not in start)
#     return end_city
#
#
# end_city = find_end_city(paths)
# print(f"{end_city} is the end.")
