import collections


def is_balanced_binary_tree(tree):
    balanced_status_with_height = collections.namedtuple(
        'balancedstatuswithheight', ('balanced', 'height'))

    # first value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return balanced_status_with_height(True, -1)    # base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # left subtree is not balanced
            return balanced_status_with_height(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # right subtree is not balanced
            return balanced_status_with_height(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return balanced_status_with_height(is_balanced, height)

    return check_balanced(tree).balanced