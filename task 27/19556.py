from math import dist

def edge(cluster):
    res=[]
    for dot in cluster:
        sum_dist = sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return max(res)[1]
with open(r'.\files\27.17.A_19566.txt') as file:
    dots = [list(map(int, i.replace))]
eps=1
cluster =[]
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)< eps:
                cluster.append(d)
                dots.remove(d)
        if len(cluster) > 4:
            cluster.append(cluster)
print([len(cluster) for cluster in cluster])
edges = []

