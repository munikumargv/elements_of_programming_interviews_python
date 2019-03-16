import collections


def lca(tree, node0, node1):
    status = collections.namedtuple('status', ('num_target_nodes', 'ancestor'))

    # returns an object consisting of an int and a node. the int field is 0,
    # 1 or 2 depending on how many of {node0, node1} are present in tree. if
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the lca.
    def lca_helper(tree, node0, node1):
        if not tree:
            return status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # found both nodes in the left subtree
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # found both nodes in the right subtree
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes + int(
                tree in (node0, node1)))
        return status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor
