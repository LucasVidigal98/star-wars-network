import json
import networkx as nx
import collections
import matplotlib.pyplot as plt
from CentralityComper import CentralityComper as CC
import os


class Graph:

    def __init__(self, network):
        self.data = self.read_network(network)
        self.G = self.create_graph()
        self.add_nodes()
        self.add_edges()
        self.n_nodes = self.G.number_of_nodes()
        self.n_edges = self.G.number_of_edges()
        self.giant = max(nx.connected_components(self.G), key=len)
        self.diameter, self.density = self.get_density_diameter()
        self.clustering = self.get_clustering()
        self.middle_degree = self.get_middle_degree()

    def read_network(self, network):
        with open('..' + os.path.sep + 'data' + os.path.sep + network, 'r') as json_file:
            data = json.load(json_file)
            return data

    def create_graph(self):
        G = nx.Graph()
        return G

    def add_nodes(self):
        nodes_list = list()
        id = 0
        for node in self.data['nodes']:
            n = (id, {'name': node['name'],
                      'colour': node['colour'], 'value': node['value']})
            id += 1
            nodes_list.append(n)
        self.G.add_nodes_from(nodes_list)

    def add_edges(self):
        edges_list = list()
        for edge in self.data['links']:
            e = (edge['source'], edge['target'], {'value': edge['value']})
            edges_list.append(e)
        self.G.add_edges_from(edges_list)

    def get_info(self):
        print('-------------------------Características Básicas-------------------------')
        print('Número de vértices = ' + str(self.n_nodes))
        print('Número de arestas = ' + str(self.n_edges))
        print('Densidade = ' + str(self.density))
        print('Diâmetro = ' + str(self.diameter))
        print('Clustering Médio = ' + str(self.clustering))
        print('Gráu médio = ' + str(self.middle_degree))
        print('-------------------------Características Básicas-------------------------')

    def get_density_diameter(self):
        density = nx.density(self.G)
        diameter = nx.diameter(self.G)
        return diameter, density

    def get_middle_degree(self):
        degrees = nx.degree(self.G)
        total = 0
        
        for degree in degrees:
            total += degree[1]

        return total / self.n_nodes

    def get_clustering(self):
        clusterings = nx.clustering(self.G)

        total = 0
        for i in range(0, len(clusterings)):
            total += clusterings[i]

        return total / self.n_nodes

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        plt.axis('off')
        node_colors = list()
        node_names = dict()

        for color in self.G.nodes(data='colour'):
            node_colors.append(color[1])

        for name in self.G.nodes(data='name'):
            node_names.update({int(name[0]): name[1]})

        nx.draw_networkx_nodes(self.G, pos, node_size=60,
                               node_color=node_colors)
        nx.draw_networkx_edges(self.G, pos, alpha=0.8)
        nx.draw_networkx_labels(
            self.G, pos, labels=node_names, font_size=8, alpha=0.5)
        plt.show()

    def degreehistogram(self):
        degree_sequence = sorted(
            [d for n, d in self.G.degree()], reverse=True)  # degree sequence
        # print "Degree sequence", degree_sequence
        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())

        fig, ax = plt.subplots()
        plt.bar(deg, cnt, width=0.80, color='b')

        plt.title("Degree Histogram")
        plt.ylabel("Count")
        plt.xlabel("Degree")
        ax.set_xticks([d + 0.4 for d in deg])
        ax.set_xticklabels(deg)

        # draw graph in inset
        plt.axes([0.4, 0.4, 0.5, 0.5])
        Gcc = sorted(nx.connected_components(self.G),
                     key=len, reverse=True)[0]
        pos = nx.spring_layout(self.G)
        plt.axis('off')
        nx.draw_networkx_nodes(self.G, pos, node_size=20)
        nx.draw_networkx_edges(self.G, pos, alpha=0.4)

        plt.show()

    def eigenvector(self):
        return nx.eigenvector_centrality(self.G, 100)

    def closeness(self):
        return nx.closeness_centrality(self.G)

    def betweeness(self):
        return nx.betweenness_centrality(self.G)

    def degree_centrality(self):
        return nx.degree_centrality(self.G)

    def centrality_ranking(self, centrality, centrality_name):
        node_names = self.G.nodes(data="name")

        nodes_list = list()
        for n in range(0, len(centrality)):
            node_data = node_names[n]
            centrality_comper = CC(node_data, centrality[n])
            nodes_list.append(centrality_comper)

        sorted_nodes = sorted(nodes_list, key=CC.get_centrality, reverse=True)

        print('-------------------------Ranking ' +
              centrality_name + '-------------------------')
        for n in range(0, len(sorted_nodes)):
            if n == 20:
                break
            print(sorted_nodes[n].node)
            print(centrality_name + ' ' + str(sorted_nodes[n].centrality))
            print('')
        print('-------------------------Ranking ' +
              centrality_name + '-------------------------')
