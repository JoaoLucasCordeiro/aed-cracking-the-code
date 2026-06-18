def has_cycle(graph: dict[str, list[str]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2

    color = {node: WHITE for node in graph}

    def visit(node: str) -> bool:
        color[node] = GRAY

        for neighbor in graph.get(node, []):

            if color.get(neighbor, WHITE) == GRAY:
                return True

            if (
                color.get(neighbor, WHITE) == WHITE
                and visit(neighbor)
            ):
                return True

        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE and visit(node):
            return True

    return False
