from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    low = min(value1, value2)
    high = max(value1, value2)

    node = root

    while node is not None:
        value = node.get_value()

        if high < value:
            node = node.get_left_child()

        elif low > value:
            node = node.get_right_child()

        else:
            return value

    return None
