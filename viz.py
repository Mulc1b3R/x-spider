import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt
import json

# Load JSON data from output.json
with open('output/output.json', 'r') as json_file:
    data = json.load(json_file)

# Create a directed graph
G = nx.DiGraph()

# Add nodes (URLs) to the graph
for item in data:
    G.add_node(item['url'])

# Add edges between nodes (URLs)
for i in range(1, len(data)):
    G.add_edge(data[i-1]['url'], data[i]['url'])

# Draw the graph
pos = nx.spring_layout(G)  # Choose a layout
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=8, font_color='black', edge_color='gray')
plt.title("Website Structure Visualization")
plt.savefig("output/website_structure.png")  # Save the plot as an image file
plt.show()