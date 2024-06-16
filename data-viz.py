import json
import networkx as nx
import matplotlib.pyplot as plt
from mpld3 import plugins

# Load data from data.json file
with open('output/data.json') as json_file:
    data = json.load(json_file)

# Create a directed graph
G = nx.DiGraph()
node_colors = {}
labels = {}

# Add nodes for target URL, metadata, analytics, backlinks, social shares
G.add_node(data['target_url'], color='blue')
node_colors[data['target_url']] = 'blue'
labels[data['target_url']] = data['target_url']

data_nodes = ['Metadata', 'Analytics', 'Backlinks', 'Social Shares']
node_colors.update({node: 'green' for node in data_nodes})
G.add_nodes_from(data_nodes)

# Add edges between target URL and data nodes
for node in data_nodes:
    G.add_edge(data['target_url'], node)

for link in data['links']:
    if link not in G.nodes:
        G.add_node(link, color='gray')
        node_colors[link] = 'gray'
        labels[link] = link
        G.add_edge(data['target_url'], link)

# Create figure and axis for the plot
fig, ax = plt.subplots()
plt.title('Data Infographic for Target URL')

# Define custom node colors
node_colors_list = [node_colors[name] for name in G.nodes]

# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=False, node_color=node_colors_list, node_size=2000, edge_color='black')

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black', font_weight='bold')

# Define plugin for hovering over the nodes
tooltip = plugins.PointHTMLTooltip(G, labels)
plugins.connect(fig, tooltip)

# Display the graph with hover-over functionality
plt.show()