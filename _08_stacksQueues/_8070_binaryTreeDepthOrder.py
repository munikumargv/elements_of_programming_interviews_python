import collections


def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                # defer the null checks to the null test above
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes
    return result
