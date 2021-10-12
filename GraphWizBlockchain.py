import csv,  glob, networkx as nx, matplotlib.pyplot as plt, pydot

rootpath = 'C:\\Test\\'
colors = ['#a6cee3', '#1f78b4','#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928']
targetPattern = rootpath+'INPUT_CSV\\*.csv'
listFiles = []
listFiles = glob.glob(targetPattern)
G = nx.DiGraph()

for list in listFiles:
    with open(list) as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader,None)
        i=0
        for row in spamreader:
            if row[7] != "0":
                G.add_edge(row[4],row[5], weight = row[7], label= row[3]+' | '+row[7], color = colors[i])
            else:
                G.add_edge(row[4],row[5], weight = row[8], label= row[3]+' | '+row[8], color = colors[i])
            if i==11: 
                i = 0
            else:
                i=i+1

nx.drawing.nx_pydot.write_dot(G, rootpath+'multi_dot.dot')
graph = nx.drawing.nx_pydot.to_pydot(G)
graph.rankdir = "TB"

graph.write_svg('output.svg', prog = 'circo')