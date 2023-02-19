import json
from PIL import Image

def Generate_Graph():
    list_ = {}
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for x in range(26):
        for y in range(26):

            if x < 26:
                name = letters[0] + " " + str(y)     
            else:
                name = str(x) + "NoT a ChArAtEr " + str(y)

            value = x*40, y*40
            list_[name] = value

        if x < 26:
            letters.pop(0)

    return list_

def Connect_Nodes(nodes, image_path):
    max_col = max(int(node.split()[1]) for node in nodes)
    adjacency_dict = {}
    
    # Load the image
    with Image.open(image_path) as im:
        im = im.convert("L")
        # Get the size of the image
        width, height = im.size
        
        for node in nodes:
            row, col = node.split()
            row_index = ord(row) - ord('A')
            col_index = int(col)
            adjacency_dict[node] = {}
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    new_row_index = row_index + i
                    new_col_index = col_index + j
                    if new_row_index < 0 or new_row_index >= max_col or new_col_index < 0 or new_col_index > max_col:
                        continue
                    new_row = chr(new_row_index + ord('A'))
                    if new_row == row and new_col_index == col_index:
                        continue
                    new_node = new_row + " " + str(new_col_index)
                    
                    # Convert the position of the new node to pixel coordinates
                    new_x, new_y = int(new_col_index*40), int(new_row_index*40)
                    px, py = int(new_x/40), int(new_y/40)
                    
                    # Check if the pixel at the new node's position is black
                    threshold = 50
                    if im.getpixel((px, py)) < threshold:
                        continue  # If the pixel is black, skip the connection

                    # Calculate the weight of the edge
                    if i == 0 or j == 0:
                        weight = 1
                    else:
                        weight = 1.41
                    
                    adjacency_dict[node][new_node] = weight
                    
    return adjacency_dict

Graph = Generate_Graph()
Node_Connections = Connect_Nodes(Graph, r"C:\Users\Tocom\OneDrive\Pictures\Camera Roll\img.png")

f = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\A-star algorithm\Graphs\Graph.json", "w")
f.write(str(json.dumps(Graph)))
f.close()

f = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\A-star algorithm\Graphs\Node_Connections.json", "w")
f.write(str(json.dumps(Node_Connections)))
f.close()