# There are many representations of graphs using Python
# Here is one example using dictioniary: https://www.python-course.eu/graphs_python.php
# Here we will use two or three lists 

class Graph(object):
    """A graph object 
    """

    def __init__(self, source_nodes, target_nodes, weights=None):

        if not isinstance(source_nodes, list):
            raise TypeError('source_nodes should be a list')

        if not isinstance(target_nodes, list):
            raise TypeError('target_nodes should be a list')

        if weights:
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
        
    
    
if __name__ == '__main__':
    
    sources = [1,2,3]
    targets = [2,3,4]
    weights = [1,1,1]

    g = Graph(source_nodes=sources, target_nodes=targets, weights=weights)

    print('nodes: ', g.nodes)
    print('edges: ', g.edges)
    
