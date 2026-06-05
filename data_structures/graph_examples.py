GRAPH_WITHOUT_CYCLE = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
}


GRAPH_WITH_CYCLE = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}


GRAPH_WITH_SELF_LOOP = {
    "A": ["A"],
}


DISCONNECTED_GRAPH = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": [],
}


DISCONNECTED_GRAPH_WITH_CYCLE = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": ["C"],
}


WEIGHTED_GRAPH = {
    "P": [
        ("E", 2),
        ("R", 4),
    ],
    "E": [
        ("R", 1),
        ("N", 7),
    ],
    "R": [
        ("M", 3),
        ("N", 2),
    ],
    "N": [
        ("O", 1),
    ],
    "M": [
        ("O", 2),
    ],
    "O": [],
}
