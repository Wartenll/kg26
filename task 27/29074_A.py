from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            stars.append(list(map(float, [x, y])))
cluster_A_1 = [d for d in stars if d[1]> 10]
cluster_A_2 = [d for d in stars if d[1]< 10]
clusters = [cluster_A_1, cluster_A_2]
A1 = min(len(cluster_A_1), len(cluster_A_2))
A2 =max(len(cluster_A_1), len(cluster_A_2))
print(A1, A2)
