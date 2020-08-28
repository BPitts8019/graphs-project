from queue import Queue


def addVertexTo(graph, vertex, data_point=None):
    if vertex not in graph:
        graph[vertex] = set()

    if data_point is not None:
        graph[vertex].add(data_point)


def getGraphFrom(input_list):
    rtn_graph = {}

    for parent, child in input_list:
        addVertexTo(rtn_graph, parent)
        addVertexTo(rtn_graph, child, parent)

    return rtn_graph


def earliest_ancestor(ancestors, starting_node):
    ancestor_data = getGraphFrom(ancestors)
    search_queue = Queue()
    visited_ancestors = set()
    earliest_ancestors = {}

    cur_ancestry = [starting_node]
    search_queue.put(cur_ancestry)
    while not search_queue.empty():
        cur_ancestry = search_queue.get()
        if cur_ancestry[-1] not in visited_ancestors:
            if not ancestor_data[cur_ancestry[-1]]:
                num_generations = len(cur_ancestry)
                if num_generations not in earliest_ancestors or cur_ancestry[-1] < earliest_ancestors[num_generations]:
                    earliest_ancestors[num_generations] = cur_ancestry[-1]

            for ancestor in ancestor_data[cur_ancestry[-1]]:
                search_queue.put(cur_ancestry + [ancestor])

            visited_ancestors.add(cur_ancestry[-1])

    if cur_ancestry[-1] == starting_node:
        return -1

    return earliest_ancestors[max(earliest_ancestors.keys())]


if __name__ == "__main__":
    ancestors = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (8, 9),
        (11, 8),
        (10, 1)
    ]

    print(earliest_ancestor(ancestors, 8))
