import networkx as nx
import csv
from networkx import Graph
import matplotlib.pyplot as plt


# Print out the list of nodes and edges with attributes.
G = nx.karate_club_graph()
print("all nodes with atttributes: ", G.nodes(data=True),"all edges: ", G.edges())


# Poviding a visualization of the Karate club where the
# color of nodes will represent the two groups after the separation.
node_color = []
for node in G.nodes(data=True):

    # Om nodene er i Mr. Hi sin klub blir fargen satt til blå
    if 'Mr. Hi' in node[1]['club']:
        node_color.append('blue')

    # Om nodene er i Officer sin klub blir fargen satt til oransje
    elif 'Officer' in node[1]['club']:
        node_color.append('orange')

    #om det er noen noder som ikke tilhører noen av klubbene blir fargen satt til grønn
    else:
        node_color.append('green')


# Task 1.3: Using nx.dijkstra_path() find out the shortest path from node 24 to 16. Print the list of nodes.
print(nx.dijkstra_path(G,24,16))
print("length of path = ", (len(nx.dijkstra_path(G,24,16)) - 1))

# color of nodes will represent the two groups after the separation
node_colors = []

# Provide a visualization of the Karate club and modify the color of the nodes
# by highlighting the selected nodes from the above list.
# Use red color to indicate the selection of the nodes
# color of nodes will represent the two groups after the separation
node_colors = []
for node in G.nodes(data=True):

    if node[0] in nx.dijkstra_path(G,24,16):
        node_colors.append('red')

    elif 'Mr. Hi' in node[1]['club']:
        node_colors.append('blue')

    elif 'Officer' in node[1]['club']:
        node_colors.append('orange')
        #om det er noen noder som ikke tilhører noen av klubbene blir fargen satt til grønn
    else:
        node_colors.append('green')




#Draws the karate_club graph of the groups seperation
nx.draw(G, node_color=node_color, with_labels=True)
plt.show()

#Draws the same graph with the path between node 16 and 24 highlighted by nodecolour
nx.draw(G, node_color=node_colors, with_labels=True)
plt.show()