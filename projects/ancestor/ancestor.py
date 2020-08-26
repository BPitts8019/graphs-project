def getGraphFrom(input_list):
    rtn_graph = {}

    for parent, child in input_list:
        if child not in rtn_graph:
            rtn_graph[child] = set()

        rtn_graph[child].add(parent)

    return rtn_graph


def earliest_ancestor(ancestors, starting_node):
    ancestor_data = getGraphFrom(ancestors)
    search_stack = [starting_node]
    visited_nodes = set()
    early_ancestors = []

    while len(search_stack) > 0:
        cur_ancestor = search_stack.pop()
        if cur_ancestor not in visited_nodes:
            if cur_ancestor in ancestor_data:
                for ancestor in ancestor_data[cur_ancestor]:
                    search_stack.append(ancestor)
            else:
                early_ancestors.append(cur_ancestor)

        visited_nodes.add(cur_ancestor)

    if cur_ancestor == starting_node:
        return -1

    return min(early_ancestors)


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

    print(earliest_ancestor(ancestors, 6))
