# There are many representations of graphs using Python
# Here is one example using dictioniary: https://www.python-course.eu/graphs_python.php
# Here we will use two or three lists 
# Though the representations are different, the logics are mostly the same.


class Graph(object):
    """A graph object 
    """

    def __init__(self, source_nodes, target_nodes, weights=None):

        if not isinstance(source_nodes, list):
            raise TypeError('source_nodes should be a list')

        if not isinstance(target_nodes, list):
            raise TypeError('target_nodes should be a list')

        if not (weights is None):
            if not isinstance(weights, list):
                raise TypeError('weights should be a list if exists otherwise should be None')

        self.source_nodes = source_nodes
        self.target_nodes = target_nodes
        self.weights = weights

        # calculate all possible nodes in the Graph
        self._nodes = self.__calculate_nodes(source_nodes, target_nodes)
        # calculate edges
        self._edges = self.__calculate_edges(source_nodes, target_nodes, weights)

    def __calculate_nodes(self, source_nodes, target_nodes):
        """calculate all the nodes from source list and target list
        """
        return list(set(self.source_nodes + self.target_nodes))

    def __calculate_edges(self, source_nodes, target_nodes, weights):
        """calculate all the nodes from source list and target list and weights if exists
        """
        edges = None
        if weights:
            edges = list(zip(source_nodes, target_nodes, weights))
        else:
            edges = list(zip(source_nodes, target_nodes))
        return edges

    @property
    def nodes(self):
        self._nodes = self.__calculate_nodes(self.source_nodes, self.target_nodes)
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        if not isinstance(nodes, (list, set)):
            raise TypeError('nodes are represented by a list')
        else:
            self._nodes = nodes

    @nodes.deleter
    def nodes(self):
        del self._nodes

    @property
    def edges(self):
        self._edges = self.__calculate_edges(self.source_nodes, self.target_nodes, self.weights)
        return self._edges

    @edges.setter
    def edges(self, edges):
        if not isinstance(edges, (list, set)):
            raise TypeError('edges are represented by a list')
        else:
            self._edges = edges

    @edges.deleter
    def edges(self):
        del self._edges

    def add_edges(self, new_sources, new_targets, new_weights):
        """add new edges to the graph
        """
        self.source_nodes = self.source_nodes + new_sources
        self.target_nodes = self.target_nodes + new_targets
        if self.weights is None:
            raise Exception('This graph has no weights assigned')
        else:
            self.weights = self.weights + new_weights

    def nodes_by_weight(self):
        """Find all nodes for each weight
        """

        weight_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = i[:2]

            i_weight_nodes = weight_dict.get(i_weight, [])

            for i_node in i_edge:
                if i_node not in i_weight_nodes:
                    i_weight_nodes.append(i_node)

            weight_dict[i_weight] = i_weight_nodes

        return weight_dict

    def edges_by_weight(self):
        """Find all edges for each weight
        """

        weight_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = tuple(sorted(i[:2]))

            i_weight_edges = weight_dict.get(i_weight, [])

            if i_edge not in i_weight_edges:
                i_weight_edges.append(i_edge)

            weight_dict[i_weight] = i_weight_edges

        return weight_dict

    def weigts_by_node_comb(self):
        """Find all the weights for each combination of nodes
        """
        edge_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = tuple(sorted(i[:2]))

            i_edge_weights = edge_dict.get(i_edge, [])

            if i_weight not in i_edge_weights:
                i_edge_weights.append(i_weight)

            edge_dict[i_edge] = i_edge_weights

        return edge_dict

    def __str__(self):
        return f"nodes: {self.nodes}\nedges: {self.edges}"
        



    
    
if __name__ == '__main__':
    
    sources = [1,2,3]
    targets = [2,3,4]
    weights = [1,1,1]

    g = Graph(source_nodes=sources, target_nodes=targets, weights=weights)

    print(g)

    new_source = [10,11]
    new_target = [1,3]
    new_weights = [1,1]
    g.add_edges(new_source, new_target, new_weights)

    print(g)

    g_null = Graph(source_nodes=[], target_nodes=[], weights=[])
    
    print(g_null)

    g_null.add_edges(new_source, new_target, new_weights)

    print(g_null)


    
