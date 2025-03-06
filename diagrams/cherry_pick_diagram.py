import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches


commit_hashes = {
    "A": "1a2b3c", "B": "4d5e6f", "C": "7g8h9i", "D": "0j1k2l",
    "X": "3m4n5o", "Y": "6p7q8r", "Z": "9s0t1u"
}

# create a directed graph
G = nx.DiGraph()

# define nodes for commits and their pos
positions = {
    # source branch commits
    "A": (0,2),
    "B": (1,2),
    "C": (2,2), # commit to be cherry-picked
    "D": (3,2),

    # destination branch commits
    "X": (0,0),
    "Y": (1,0),
    "Z": (3,0) # after cherry-pick, commit C will be here
}

# add nodes
G.add_nodes_from(positions.keys())

# add edges (b4 cherry-pick)
edges_before = [("A", "B"), ("B", "C"), ("C", "D"), ("X", "Y")]
G.add_edges_from(edges_before)

# create fig with two subplots
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

#-----------------------------------------

### **b4 cherry-pick**
ax = axes[0]
axes[0].set_xlim(-1, 4)
axes[0].set_ylim(-1, 3)
ax.set_title("Before Cherry-Pick", fontsize=12, fontweight="bold", fontfamily="Courier New")

nx.draw(G, pos=positions, with_labels=False, node_color="black", edge_color="black", node_size=2000, font_size=12, font_family="Courier New", ax=ax)
nx.draw_networkx_labels(G, pos=positions, labels=commit_hashes, font_color="white", font_size=10, font_family="Courier New", ax=ax)

# faded node z to showcase commit doesnt exist yet
nx.draw_networkx_nodes(G, pos=positions, nodelist=["Z"], node_color="lightgray", node_size=2000, alpha=0.5, ax=ax)
ax.annotate("doesn't exist yet", 
            xy=(3.03, 0.3), xytext=(2.5, 0.8), bbox=dict(facecolor="white", edgecolor="gray", alpha=0.7),
            fontsize=7, fontweight="bold", color="gray", fontfamily="Courier New",
            arrowprops=dict(arrowstyle="->", color="gray"))

# labels to showcase branches on 'before' diagram
ax.text(-0.3, 2.6, "branch-1 (source)", fontsize=8, fontweight="bold", bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")
ax.text(-0.3, -0.6, "branch-2 (destination)", fontsize=8, fontweight="bold", bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")

# border for diagram
rect_before = patches.Rectangle((0, 0), 1, 1, linewidth=2.5, edgecolor="black", facecolor="none", transform=ax.transAxes)
ax.add_patch(rect_before)

#-----------------------------------------

### **after cherry-pick**

# simulate cherry-picking by adding commit c to dest branch
G.add_edge("Y", "Z") # connect dest branch to new commit

ax = axes[1]
axes[1].set_xlim(-1, 4)
axes[1].set_ylim(-1, 3)
ax.set_title("After Cherry-Pick", fontsize=12, fontweight="bold", fontfamily="Courier New")

nx.draw(G, pos=positions, with_labels=False, node_color="black", font_color="white", edge_color="black", node_size=2000, font_size=12, font_family="Courier New", ax=ax)
nx.draw_networkx_labels(G, pos=positions, labels=commit_hashes, font_color="white", font_size=10, font_family="Courier New")

# highlighted node to show its the commit that is cherry-picked
nx.draw_networkx_nodes(G, pos=positions, nodelist=["C"], node_color="red", node_size=2000, alpha=0.5, ax=ax)

nx.draw_networkx_nodes(G, pos=positions, nodelist=["Z"], node_color="green", node_size=2000, alpha=0.5, ax=ax)

nx.draw_networkx_edges(G, pos=positions, edgelist=[("C", "Z")], style="dashed", edge_color="gray", ax=ax)

# add labels to 'after' diagram
ax.text(-0.3, 2.6, "branch-1 (source)", fontsize=8, fontweight="bold", bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")
ax.text(-0.3, -0.6, "branch-2 (destination)", fontsize=8, fontweight="bold", bbox=dict(facecolor="white", alpha=0.7), fontfamily="Courier New")

# commit c label
ax.annotate("original commit\n(cherry-picked from here)", 
            xy=(2.3, 2.1), xytext=(2.1, 2.6), bbox=dict(facecolor="white", edgecolor="darkred", alpha=0.7),
            fontsize=7, fontweight="bold", color="darkred", fontfamily="Courier New",
            arrowprops=dict(arrowstyle="->", color="darkred"))

# commit z label
ax.annotate("new commit\n(cherry-picked copy)", 
            xy=(2.9, -0.3), xytext=(2.2, -0.8), bbox=dict(facecolor="white", edgecolor="darkgreen", alpha=0.7),
            fontsize=7, fontweight="bold", color="darkgreen", fontfamily="Courier New",
            arrowprops=dict(arrowstyle="->", color="darkgreen"))

# commit operation
ax.annotate("cherry-pick operation\n(copied commit)", 
            xy=(2.5, 0.9), xytext=(0.7, 0.8), bbox=dict(facecolor="white", edgecolor="gray", alpha=0.7, linestyle="dashed"),
            fontsize=7, fontweight="bold", color="gray", fontfamily="Courier New",
            arrowprops=dict(arrowstyle="->", linestyle="dashed", color="gray"))

# border for diagram
rect_after = patches.Rectangle((0, 0), 1, 1, linewidth=2.5, edgecolor="black", facecolor="none", transform=ax.transAxes)
ax.add_patch(rect_after)

# show the diagram
plt.show()