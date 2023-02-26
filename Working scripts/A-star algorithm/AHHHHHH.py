import pygame, sys, random
import heapq, json, os

def a_star(start, goal, graph):
    # check if the start and goal node present in the graph or not
    if start not in graph or goal not in graph:
        return None, None
    # Create an empty priority queue
    queue = []
    # Push the starting point into the queue with a priority of 0
    heapq.heappush(queue, (0, start))
    # Create a dictionary to store the cost of each point
    cost = {start: 0}
    # Create a dictionary to store the parent of each point
    parent = {start: None}
    while queue:
        # Pop the point with the lowest priority from the queue
        current = heapq.heappop(queue)[1]
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
                heapq.heappush(queue, (priority, neighbor))

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

#test the function

# Define node positions
Node_Connections = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\A-star algorithm\Graphs\Node_Connections.json", "r")
Graph_file = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\A-star algorithm\Graphs\Graph.json", "r")

Node_Connection = Graph_file.read()
Graph = Node_Connections.read()

Node_Connections.close()
Graph_file.close()

node_pos = json.loads(Node_Connection)
graph = json.loads(Graph)

image = pygame.image.load(r"C:\Users\Tocom\OneDrive\Pictures\Camera Roll\map.png")

# Get the current width and height of the image
original_width, original_height = image.get_size()

# Scale up the image
image = pygame.transform.scale(image, (int(original_width * 1.16), int(original_height * 1.16)))


#---------------------

start = 'A 0'
goal =  'A 1'

def random_goal():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    start = letters[random.randrange(0,25)] + " " + str(random.randrange(0,25))
    goal = letters[random.randrange(0,25)] + " " + str(random.randrange(0,25))

    return start, goal

#---------------------

start, goal = random_goal()

path, cost = a_star(start, goal, graph)
clock = pygame.time.Clock()

if path is None:
    print("Error: Start or goal node not found in the graph")
else:
    # Initialize Pygame
    pygame.init()


    size = 26/2
    font = pygame.font.Font(None, 13)

    # Create a window
    width = 800*1.3
    height = 800*1.3
    screen = pygame.display.set_mode((width, height))
    # print final cost
    print("Final cost:", round(cost[goal],2))
    # Draw the graph
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    try:
                        start, goal = random_goal()
                        path, cost = a_star(start, goal, graph)
                        os.system('cls')
                        print("Final cost:", round(cost[goal],2))
                    except:
                        print("Error: Start or goal node not found in the graph")
        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the image
        screen.blit(image, (0,0))

        # Draw edges
        for node1 in graph:
            for node2 in graph[node1]:
                pygame.draw.line(screen, (0, 0, 255), node_pos[node1], node_pos[node2], 2)
        # Draw nodes

        for node1 in graph:
            for node2 in graph[node1]:
                pygame.draw.circle(screen, (0, 0, 0), node_pos[node1], 5)
                try:
                    if node1 in path and node2 in path:
                        if path.index(node1) == path.index(node2) - 1:
                            pygame.draw.line(screen, (255, 0, 0), node_pos[node1], node_pos[node2], 4)
                except:
                    raise RuntimeError("Error: Start or goal node not found in the graph")
        # Draw labels
        for node in graph:
            label = font.render(node, 1, (0, 0, 0))
            screen.blit(label, (node_pos[node][0] + 5, node_pos[node][1] + 5))
        
        # Update the screen
        pygame.display.update()
        clock.tick(10)
