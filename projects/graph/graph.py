"""
Simple graph implementation
"""
from queue import Queue, LifoQueue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            print(f"{v1} doesn't exist")
            return

        if v2 not in self.vertices:
            print(f"{v2} doesn't exist")
            return

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

        return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        search_queue = Queue()
        visited_verticies = set()

        search_queue.put(starting_vertex)
        while not search_queue.empty():
            cur_vertex = search_queue.get()
            if cur_vertex not in visited_verticies:
                print(cur_vertex)
                visited_verticies.add(cur_vertex)
                for connection in self.get_neighbors(cur_vertex):
                    search_queue.put(connection)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        search_stack = LifoQueue()
        visited_verticies = set()

        search_stack.put(starting_vertex)
        while not search_stack.empty():
            cur_vertex = search_stack.get()
            if cur_vertex not in visited_verticies:
                print(cur_vertex)
                visited_verticies.add(cur_vertex)
                for connection in self.get_neighbors(cur_vertex):
                    search_stack.put(connection)

    def dft_recursive(self, cur_vertex, visited_verticies=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if cur_vertex in visited_verticies:
            return

        print(cur_vertex)
        visited_verticies.add(cur_vertex)
        for connection in self.get_neighbors(cur_vertex):
            self.dft_recursive(connection, visited_verticies)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the path to starting vertex (list)
        # create an empty visited_set

        # while the queue is not empty
        #    get current vertex Path (dequeue from queue)
        #    set the current vertext to the LAST element of the path

        #    If current vetex is destination_vertex
        #       STOP and return path

        #    mark current vertex as visited - add to a visited_set
        #    for each connection if connection is not in visited_set
        #       enqueue a new path with connection appended
        search_queue = Queue()
        visited_verticies = set()

        search_queue.put([starting_vertex])
        while not search_queue.empty():
            cur_path = search_queue.get()

            if cur_path[-1] == destination_vertex:
                return cur_path

            if cur_path[-1] not in visited_verticies:
                visited_verticies.add(cur_path[-1])
                for connection in self.get_neighbors(cur_path[-1]):
                    search_queue.put(cur_path + [connection])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(2, 8)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(8, 4)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
