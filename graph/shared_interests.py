from base import Graph
from itertools import combinations


class Interests():
    """An object for a group of people connected by interests
    """

    def __init__(self, users_1, users_2, interests):
        # super().__init__(users_1, users_2, interests)
        self.interest_graph = Graph(users_1, users_2, interests)

    @staticmethod
    def _reconstruct_edges_from_nodes(nodes):
        """Given a list of nodes, construct all possible edges
        """
        return list(combinations(sorted(nodes), 2))

    def construct_full_interest_graph(self):
        """Calculates the full interest graph

        If 1 and 2 share interest A and 2 and 3 share interest A too, 
        we will connect 1 and 3 with interest A.
        """

        nodes_by_interests = self.interest_graph.nodes_by_weight()

        full_interest_graph = Graph([], [], [])

        for interest, nodes in nodes_by_interests.items():
            for edge in self._reconstruct_edges_from_nodes(nodes):
                full_interest_graph.add_edges([edge[0]], [edge[1]], [interest])

        self.full_interest_graph = full_interest_graph

        return full_interest_graph


if __name__ == '__main__':
    source_nodes = [1, 1, 2, 3, 2]
    target_nodes = [2, 3, 4, 5, 4]
    interests = ['A', 'B', 'A', 'C', 'B']

    it = Interests(source_nodes, target_nodes, interests)
    print(it.interest_graph)

    print(it._reconstruct_edges_from_nodes([1,2,3, 5,4]))

    print('full graph\n', it.construct_full_interest_graph())

    print('full graph weight by node combinations:\n',it.full_interest_graph.weigts_by_node_comb())
    
    print('full graph nodes_by_weight:\n', it.full_interest_graph.nodes_by_weight())

    print('full graph edges_by_weight:\n', it.full_interest_graph.edges_by_weight())


