from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
            stars.append(list(map(float, [x, y])))


cluster_1 = [[d for d in dots if 23 < d[1]],
             [d for d in stars if 23 < d[1]]]
cluster_2 = [[d for d in dots if 15 < d[1] < 23],
             [d for d in stars if 15 < d[1] < 23]]
cluster_3 = [[d for d in dots if d[1] < 15],
             [d for d in stars if d[1] < 15]]
clusters = [cluster_1, cluster_2, cluster_3]

dists = []
for cluster in clusters:
    dists += [dist(center(cluster[0]), s) for s in cluster[1]]
print(min(dists) * 10_000, max(dists) * 10_000)


