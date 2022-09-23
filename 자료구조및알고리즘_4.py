from collections import defaultdict
from heapq import *

# Problem1
def prim_al(start, edges):
    mst = list()
    adj_edge = defaultdict(list)
    for n1, n2, weight in edges:
        adj_edge[n1].append((n1, n2, weight))
        adj_edge[n2].append((n2, n1, weight))

    con_node = set(start)
    edge_list = adj_edge[start]

    while edge_list:
        edge_list.sort(key=lambda x: x[-1])
        n1, n2, weight = heappop(edge_list)
        if n2 not in con_node:
            con_node.add(n2)
            mst.append((n1, n2, weight))

            for edge in adj_edge[n2]:
                if edge[1] not in con_node:
                    heappush(edge_list, edge)

    return mst

info = [('0', '1', 4), ('0', '2', 3), ('1', '2', 2), ('2', '3', 1), ('3', '4', 1), ('3', '5', 5), ('4', '5', 6)]
print(prim_al('3', info))


# Problem2
def bridge(n, costs):
    result = 0
    costs.sort(key = lambda x: x[2])
    routes = set([costs[0][0]])

    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                result += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return result


isl = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,6]]
print(bridge(4, isl))