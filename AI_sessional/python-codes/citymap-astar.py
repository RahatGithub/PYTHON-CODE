# citymap with astar

from queue import PriorityQueue
import math

points = {'A': (1, 9),
          'B': (2, 4),
          'C': (5, 8),
          'D': (11, 2),
          'E': (7, 11),
          'F': (6, 6),
          'G': (4, 2),
          'H': (9, 8),
          'I': (10, 6),
          'J': (12, 10),
          'K': (8, 3),
          'L': (9, 1),
          'M': (12, 1),
          'N': (4, 5),
          'S': (2, 7)
          }
# distance_uv = round(math.sqrt((points['S'][0]-points['A'][0])**2 + (points['S'][1]-points['A'][1])**2)) #points[u]-points[v]
# print(distance_uv)

h = {'A': {'E': 60},
     'B': {'G': 30},
     'C': {'N': 50, 'E': 30},
     'D': {'M': 20},
     'E': {'H': 50, 'J': 60},
     'F': {'I': 50},
     'G': {'K': 50},
     'H': {'D': 90},
     'I': {},
     'J': {'D': 100},
     'K': {'I': 50, 'L': 30},
     'L': {'D': 30},
     'M': {},
     'N': {'F': 40, 'K': 60},
     'S': {'A': 20, 'B': 30, 'C': 30}
     }


def astar(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}

    astar_traversal_output = []
    frontier = PriorityQueue()

    for city in h.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    frontier.put((h[startingCity], startingCity))

    while not frontier.empty():
        # print(frontier.get())
        u = frontier.get()[1]
        # print(u)
        astar_traversal_output.append(u)
        if u == destinationNode:
            break
        visited[u] = True
        for v in h[u].keys():
            if not visited[v]:
                # print(u+" : "+v)
                parent[v] = u
                distance_uv = round(math.sqrt((points[u][0] - points[v][0]) ** 2 + (points[u][1] - points[v][1]) ** 2), 2)
                distance[v] = distance[u] + distance_uv
                # print(points[u][v])
                # print(distance[u])
                # print(distance[v])
                frontier.put((distance[v] + h[u][v], v))
                # print(frontier.get())

    # print(parent)
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        # print(path)
        g = parent[g]
        # print(path)

    path.reverse()
    print("Path:", path)
    print("Path Cost:", distance[destinationNode])
    print("Visited City:", astar_traversal_output)
    print("Visited City Count:", len(astar_traversal_output))

src, dest = input("Enter source and destination: ").split(" ")
astar('S', 'D')