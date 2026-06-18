def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = {}

    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())
