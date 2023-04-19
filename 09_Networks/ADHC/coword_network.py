# Developed by Research and Data Services, University of Alabama Libraries
# By Avery Fernandez
# Last updated: 2023-04-19

# Import modules
import networkx as nx
import matplotlib.pyplot as plt

# Define class
class Coword_Network:
    # Initialize class with filtered pairs as input
    def __init__(self, filtered_pairs):
        # Verify the filtered_pairs format
        for pair in filtered_pairs.items():
            if not (isinstance(pair, tuple) and len(pair) == 2 and
                    isinstance(pair[0], tuple) and len(pair[0]) == 2 and
                    all(isinstance(s, str) for s in pair[0]) and
                    isinstance(pair[1], int)):
                raise ValueError(f"Invalid value: {pair}\n"+ "Invalid format: filtered_pairs must be a dictionary of tuples with the pattern {(String1, String2): Integer, ...}")
        
        # Assign filtered_pairs to class variable
        self.filtered_pairs = filtered_pairs

        # Create main graph
        self.main_graph = self.create_main_graph()

        # Create list of connected graphs from main graph
        self.connected_graphs = [self.main_graph.subgraph(c).copy() for c in nx.connected_components(self.main_graph)]

        # Create list of sorted graphs
        self.sorted_graphs = self.calculate_graph_sizes()

        # Create focused graph
        self.focused_graph = self.create_focused_graph()

    # Function to create main graph
    def create_main_graph(self):
        G = nx.Graph()
        for key, value in self.filtered_pairs.items():
            G.add_edge(key[0], key[1], weight=value)
        
        return G
    
    # Function to display main graph
    def display_main_graph(self):
        nx.draw_spring(self.main_graph, edgecolors="black", node_size=40)

    # Function to calculate graph sizes
    def calculate_graph_sizes(self):
        graph_sizes = []
        for idx, i in enumerate(self.connected_graphs):
            size = nx.number_of_nodes(i)
            graph_sizes.append((idx, size))

        return sorted(graph_sizes, key=lambda x: x[1], reverse=True)

    # Function to create focused graph
    def create_focused_graph(self):
        H = self.connected_graphs[self.sorted_graphs[0][0]]
        return H
    
    # Function to display focused graph
    def display_focused_graph(self):
        # Get node sizes
        node_sizes = {}
        for nodes in self.focused_graph.edges(data=True):
            word1, word2, size = nodes

            if word1 in node_sizes.keys():
                node_sizes[word1] += size["weight"]
            else:
                node_sizes[word1] = size["weight"]

            if word2 in node_sizes.keys():
                node_sizes[word2] += size["weight"]
            else:
                node_sizes[word2] = size["weight"]

        node_sizes = dict(node_sizes.items())

        max_node_size = max(node_sizes.values())
        scaling_factor = 200 / max_node_size

        custom_sizes = []
        for nodes in self.focused_graph.nodes:
            custom_sizes.append(node_sizes[nodes] * scaling_factor)


        # Get edge weights
        edge_weights = [d["weight"] for (_, _, d) in self.focused_graph.edges(data=True)]   

        # Calculate the minimum and maximum edge weights and the range
        min_weight = min(edge_weights)
        max_weight = max(edge_weights)
        weight_range = max_weight - min_weight

        # Define the ranges for thick, medium, and thin edges
        thin_threshold = min_weight + weight_range / 3
        medium_threshold = min_weight + 2 * weight_range / 3

        # Categorize edges based on the calculated thresholds
        thick = [(u, v) for (u, v, d) in self.focused_graph.edges(data=True) if d["weight"] > medium_threshold]
        medium = [(u, v) for (u, v, d) in self.focused_graph.edges(data=True) if thin_threshold < d["weight"] <= medium_threshold]
        thin = [(u, v) for (u, v, d) in self.focused_graph.edges(data=True) if d["weight"] <= thin_threshold]


        table_data = []
        custom_labels = {}
        for idx, nodes in enumerate(self.focused_graph.nodes(data=True)):
            custom_labels[nodes[0]] = str(nodes[0])
            table_data.append([idx, nodes[0]])

        fig, ax = plt.subplots(figsize=(12, 12))

        pos = nx.spring_layout(self.focused_graph, k=2)

        nx.draw_networkx_nodes(self.focused_graph, pos, ax=ax, edgecolors="purple", node_color="plum", node_size=custom_sizes)

        nx.draw_networkx_labels(self.focused_graph, pos, custom_labels, ax=ax)

        nx.draw_networkx_edges(self.focused_graph, pos, ax=ax, edgelist=thick, width=4, edge_color="indigo")
        nx.draw_networkx_edges(self.focused_graph, pos, ax=ax, edgelist=medium, width=3, edge_color="mediumpurple")
        nx.draw_networkx_edges(self.focused_graph, pos, ax=ax, edgelist=thin, width=2, edge_color="thistle")

        plt.axis("off")

        plt.tight_layout()

        plt.show()

    # Function to display selected network
    # Input is a graph index
    def display_selected_network(self, selected_graph):
        I = self.connected_graphs[selected_graph]
        # Get node sizes
        node_sizes = {}
        for nodes in I.edges(data=True):
            word1, word2, size = nodes

            if word1 in node_sizes.keys():
                node_sizes[word1] += size["weight"]
            else:
                node_sizes[word1] = size["weight"]

            if word2 in node_sizes.keys():
                node_sizes[word2] += size["weight"]
            else:
                node_sizes[word2] = size["weight"]

        node_sizes = dict(node_sizes.items())

        max_node_size = max(node_sizes.values())
        scaling_factor = 200 / max_node_size

        custom_sizes = []
        for nodes in I.nodes:
            custom_sizes.append(node_sizes[nodes] * scaling_factor)


        # Get edge weights
        edge_weights = [d["weight"] for (_, _, d) in I.edges(data=True)]   

        # Calculate the minimum and maximum edge weights and the range
        min_weight = min(edge_weights)
        max_weight = max(edge_weights)
        weight_range = max_weight - min_weight

        # Define the ranges for thick, medium, and thin edges
        thin_threshold = min_weight + weight_range / 3
        medium_threshold = min_weight + 2 * weight_range / 3

        # Categorize edges based on the calculated thresholds
        thick = [(u, v) for (u, v, d) in I.edges(data=True) if d["weight"] > medium_threshold]
        medium = [(u, v) for (u, v, d) in I.edges(data=True) if thin_threshold < d["weight"] <= medium_threshold]
        thin = [(u, v) for (u, v, d) in I.edges(data=True) if d["weight"] <= thin_threshold]


        table_data = []
        custom_labels = {}
        for idx, nodes in enumerate(I.nodes(data=True)):
            custom_labels[nodes[0]] = str(nodes[0])
            table_data.append([idx, nodes[0]])

        fig, ax = plt.subplots(figsize=(12, 12))

        pos = nx.spring_layout(I, k=2)

        nx.draw_networkx_nodes(I, pos, ax=ax, edgecolors="purple", node_color="plum", node_size=custom_sizes)

        nx.draw_networkx_labels(I, pos, custom_labels, ax=ax)

        nx.draw_networkx_edges(I, pos, ax=ax, edgelist=thick, width=4, edge_color="indigo")
        nx.draw_networkx_edges(I, pos, ax=ax, edgelist=medium, width=3, edge_color="mediumpurple")
        nx.draw_networkx_edges(I, pos, ax=ax, edgelist=thin, width=2, edge_color="thistle")

        plt.axis("off")

        plt.tight_layout()

        plt.show()



if __name__ == "__main__":
    filtered_pairs = {('south', 'ern'): 369,
                  ('ala', 'bama'): 3388,
                  ('john', 'w'): 521,
                  ('well', 'known'): 937,
                  ('united', 'states'): 3793,
                  ('cents', 'per'): 327,
                  ('san', 'francisco'): 350,
                  ('new', 'york'): 4592,
                  ('two', 'years'): 938,
                  ('executive', 'committee'): 520,
                  ('first', 'time'): 525}

    from coword_network import Coword_Network
    networks = Coword_Network(filtered_pairs)
    networks.display_main_graph()
    networks.display_focused_graph()

