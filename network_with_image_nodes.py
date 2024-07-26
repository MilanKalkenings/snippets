# visualize a graph using pngs as nodes

from pyvis.network import Network
import networkx as nx


G = nx.Graph()
net = Network(notebook=True)

G.add_node("node_1", title="node_1", image="icons/1.png", shape="image")
G.add_node("node_2", title="node_2", image="icons/2.png", shape="image")
G.add_edge("node_1", "node_2")


net.from_nx(G)
net.set_options("""
var options = {
  "nodes": {
    "shape": "dot",
    "size": 1024,
    "font": {
      "size": 4,
      "face": "Tahoma"
    }
  },
  "edges": {
    "width": 1
  },
  "interaction": {
    "hover": true,
    "navigationButtons": true,
    "keyboard": true
  }
}
""")
net.show("interactive_graph.html")
