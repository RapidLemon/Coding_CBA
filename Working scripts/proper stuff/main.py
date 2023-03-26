from argparse import ArgumentParser
from json import loads

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def heappop(heap):
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def a_star(start, goal, graph):
    # check if the start and goal node present in the graph or not
    if start not in graph or goal not in graph:
        return None, None
    # Create an empty priority queue
    queue = []
    # Push the starting point into the queue with a priority of 0
    heappush(queue, (0, start))
    # Create a dictionary to store the cost of each point
    cost = {start: 0}
    # Create a dictionary to store the parent of each point
    parent = {start: None}
    while queue:
        # Pop the point with the lowest priority from the queue
        current = heappop(queue)[1]
        # If the current point is the goal, we have found a path
        if current == goal:
            return construct_path(parent, goal), cost
        # Iterate over the neighbors of the current point
        for neighbor in graph[current]:
            # Calculate the new cost to reach the neighbor
            new_cost = cost[current] + graph[current][neighbor]
            # If the neighbor has not been visited or the new cost is less than the previous cost
            if neighbor not in cost or new_cost < cost[neighbor]:
                # Update the cost of the neighbor
                cost[neighbor] = new_cost
                # Update the parent of the neighbor
                parent[neighbor] = current
                # Calculate the priority of the neighbor
                priority = new_cost + heuristic(goal, neighbor)
                # Push the neighbor into the queue with the calculated priority
                heappush(queue, (priority, neighbor))

    # if the goal node is not reached return None
    return None, None

def construct_path(parent, goal):
    path = [goal]
    current = goal
    while current in parent:
        current = parent[current]
        path.append(current)
    return path[::-1]

def heuristic(goal, neighbor):
    goal_x, goal_y = node_pos[goal]
    neighbor_x, neighbor_y = node_pos[neighbor]
    return abs(goal_x - neighbor_x) + abs(goal_y - neighbor_y)

def parse_args():
    parser = ArgumentParser(description='A* algorithm')
    parser.add_argument('--start', type=str, required=True, help='Starting node')
    parser.add_argument('--goal', type=str, required=True, help='Goal node')
    return parser.parse_args()

x = parse_args()
start = x.start
goal = x.goal

Node_Connections = open(r"Node_Connections.json", "r")
Graph_file = open(r"Graph.json", "r")

Node_Connection = Graph_file.read()
Graph = Node_Connections.read()

Node_Connections.close()
Graph_file.close()

node_pos = loads(Node_Connection)
graph = loads(Graph)

path, cost = a_star(start, goal, graph)

if path is None:
    print("Error: Start or goal node not found in the graph")
else:
    for node in path:
        if path[0] == node: continue
        print(node, end=",")