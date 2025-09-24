def select_names_starting_with_M(names: list[str], case_sensitive: bool = False) -> list[str]:
    if case_sensitive:
        return [name for name in names if name and name.startswith('M')]
    else:
        return [name for name in names if name and name.lower().startswith('m')]
