from typing import Final
import numpy as np
import sys
from queue import Queue

INF: Final = sys.maxsize


def distance_cities(city1, city2, map):
    return map[city1][city2]


def uniform_cost_search(source, destination, n, cities):
    cost = np.empty(n)
    cost.fill(INF)

    parent = np.empty(n, dtype=int)
    parent.fill(0)

    priority_que = Queue()
    priority_que.put(source)

    cost[source] = 0

    while not priority_que.empty():
        current = priority_que.get()
        for child in range(0, 23):
            if cost[child] > (cost[current] + distance_cities(current, child, cities)):
                priority_que.put(child)
                cost[child] = cost[current] + \
                    distance_cities(current, child, cities)
                parent[child] = current
            #print(f'child: {child}')

    #print(f'parent: {parent}')
    path = []
    node = int(destination)
    cost_dest = cost[node]

    while (node in parent) and node != 0:
        path.append(node)
        node = int(parent[node])

    path.reverse()
    #print(f'Path: {path}\nCost dest: {cost_dest}\n')

    return path, cost_dest
