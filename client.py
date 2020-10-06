# ---------------------------------------------------
# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Project
#
# Consulted Python Documentation
# ---------------------------------------------------
import networkx as nx
from matplotlib import cm, colors, pyplot as plt 
from matpy import Matrix

# blue to red heat color map
heat_cm = colors.LinearSegmentedColormap.from_list("heat",["#00c2fc","#fc1100"])

'''
Takes in a graph instance.
Builds graph from command line input while prompting user.
'''
def graphInputBuilder(grph):

    numNodes = int(input("Number of Nodes? "))
    for i in range(1, numNodes + 1): #hide zero indexing from user
        grph.add_node(i) 

    numEdges = int(input("Number of Edges? "))
    for i in range(1, numEdges + 1):  
        temp = input(f"Which nodes (1-{numNodes}) are in edge #{i}? ")
        a, b = map(int, temp.split())
        grph.add_edge(a, b)

'''
Creates graph visualization using matplotlib given a graph, list of probabilites and title.
'''
def drawGraph(grph, probs, title):
    nx.draw_networkx(grph, pos = nx.circular_layout(G), node_color=probs, 
                    cmap=heat_cm, vmin = 0, vmax = 0.4, font_size=10)
    plt.title(title)
    plt.show()  # display in the matplotlib window

'''
Takes in a graph instance and asks for which node to random walk from and
the number of steps in the random walk.
Makes dictionary that maps nodes to probability of ending spot of random walk.
Does this by creating adjacency matrix and raising to the length of the walk.
Returns a list of node probabilites, a dict of node labels and a relevant plot title
'''
def calculate_walk(grph):
    numNodes = grph.number_of_nodes()

    strtNode = int(input("Which node do you want to random walk from? "))
    assert 1 <= strtNode <= numNodes
    steps = int(input("How many steps in your random walk? "))
    plot_title = f'{steps} Step Random Walk Starting From Node #{strtNode}'


    aDictLists = nx.to_dict_of_lists(G)

    adjMtrx = [[j-j for j in range(numNodes)] for i in range(numNodes)]

    for i in range(1, numNodes+1):
        for node in aDictLists[i]:
            adjMtrx[i-1][node-1] = 1
            adjMtrx[node-1][i-1] = 1

    adjMtrx = Matrix(adjMtrx)

    adjMtrx = adjMtrx ** steps

    ssum = 0 
    for i in range(numNodes):
        ssum += adjMtrx[strtNode-1,i]

    label_dict = {}
    probs = []
    for i in range(1, numNodes+1):
        prob = round(adjMtrx[strtNode-1,i-1] / ssum, 3)
        label_dict[i] = f"{i}\n{prob}"
        probs.append(prob)

    return probs, label_dict, plot_title

if __name__ == "__main__":
    G=nx.Graph()
    graphInputBuilder(G)
    probs, label_dict, title = calculate_walk(G)
    G = nx.relabel_nodes(G, label_dict, copy=False)
    drawGraph(G, probs, title)
