from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_B_1 = [d for d in dots if d[1] < -(19 / 12) * d[0] - 19]
cluster_B_2 = [d for d in dots if d[1] > -(19 / 12) * d[0] - 19 and d[0] < -10]
cluster_B_3 = [d for d in dots if d[0] > -10 and d[1] > (10 / 7) * d[0] + 10]
cluster_B_4 = [d for d in dots if d[1] < (10 / 7) * d[0] + 10 and d[1] > d[0]]
cluster_B_5 = [d for d in dots if d[1] < d[0] and d[1] > -5]
cluster_B_6 = [d for d in dots if d[1] < -5]
clusters = [cluster_B_1, cluster_B_2, cluster_B_3, cluster_B_4, cluster_B_5, cluster_B_6]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)
