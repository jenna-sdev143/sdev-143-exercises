import networkx as nx
import matplotlib.pyplot as plt

# create a directed graph
G = nx.DiGraph()

# add nodes 
nodes = {
    "Git (Local)": (0, 2),
    "GitHub (Remote)": (1, 1),
    "Commit": (0, 0),
    "Push": (1, 0),
    "Pull": (1, 2),
    "Dev A": (0.5, 1.5),
    "Dev B": (0.5, 0.4),
}

# define edges/show interactions
edges = [
    ("Git (Local)", "Commit"),
    ("Commit", "Git (Local)"),
    ("Git (Local)", "Push"),
    ("Push", "GitHub (Remote)"),
    ("GitHub (Remote)", "Pull"),
    ("Pull", "Git (Local)"),
    ("Dev A", "Commit"), # dev a commits changes
    ("Dev B", "Push"), # dev b pushes changes
    ("Pull", "Dev A"), # dev a pulls changes
]

# add nodes and edges to graph
G.add_nodes_from(nodes.keys())
G.add_edges_from(edges)


# define edge labels to have descriptions for each action
edge_labels = {
    ("Git (Local)", "Commit"): "Save changes",
    ("Commit", "Git (Local)"): "Version control",
    ("Git (Local)", "Push"): "Upload changes",
    ("Push", "GitHub (Remote)"): "Store remotely",
    ("GitHub (Remote)", "Pull"): "Get updates",
    ("Pull", "Git (Local)"): "Sync code",
    ("Dev A", "Commit"): "Developer A commits changes",
    ("Dev B", "Push"): "Developer B pushes code",
    ("Dev A", "Pull"): "Developer A pulls updates",
}


# draw graph
plt.figure(figsize=(8, 8))
pos = nodes # node posistions
nx.draw(G, pos, with_labels=True, node_color="black", edge_color="black", node_size=5500, font_size=8, font_weight="bold", font_family="Courier New", linewidths=2, font_color="white")

# draw dev nodes with diff shape
dev_nodes = ["Dev A", "Dev B"]
nx.draw_networkx_nodes(G, pos, nodelist=dev_nodes, node_size=4500, node_color="#333333", node_shape='*', label="Developer")

# draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color="black", font_family="Courier New")

# add annotations
plt.text(0.1, 2.1, "Local Git Repository\n(Version Control on Developer's PC)",
         fontsize=8, bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")
plt.text(0.65, 1.2, "GitHub (Remote Repo)\n(Cloud-based Collaboration)",
         fontsize=8, bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")
plt.text(0.09, 0.12, "Commit: Save changes locally",
         fontsize=8, bbox=dict(facecolor="white", alpha=0.5), fontfamily="Courier New")
plt.text(0.6, -0.1, "Push: Upload code to GitHub",
         fontsize=8, bbox=dict(facecolor="white", alpha=0.5), fontfamily="Courier New")
plt.text(0.65, 2.1, "Pull: Get latest changes",
         fontsize=8, bbox=dict(facecolor="white", alpha=0.5), fontfamily="Courier New")
plt.title("Git & GitHub Relationship")
plt.show()