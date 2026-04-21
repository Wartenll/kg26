from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open(r'.\files\27_A_21599 (1).txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]
cluster_A_1 = [d for d in dots if d[1] < -6]
cluster_A_2 = [d for d in dots if -6 < d[1] < 10/12 * d[0] - 10]
cluster_A_3 = [d for d in dots if 10/12 * d[0] - 10 < d[1]]
clusters = [cluster_A_1, cluster_A_2, cluster_A_3]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)