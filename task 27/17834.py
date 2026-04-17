from math import dist


def center(cluster):  # 2 usages
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_17834 (1).txt') as file:
    dots = [list(map(float, i.split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < 6 and dot[1] > -3]
cluster_2 = [dot for dot in dots if dot[1] > 2 and dot[1] < 12]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print((center_1[0] + center_2[0]) / 2 * 100)
print((center_1[1] + center_2[1]) / 2 * 100)
