def select_names_starting_with_M(names: list[str], case_sensitive: bool = False) -> list[str]:
    """
    Selects strings from a list of names that start with the letter 'M'.

    Args:
        names: A list of strings (names) to filter.
        case_sensitive: If True, only matches 'M'.
                        If False (default), matches 'M' or 'm'.

    Returns:
        A new list containing only the names that start with 'M' (or 'm').
    """
    # Use a list comprehension for a clean and efficient filter operation.
    # The 'name and' check handles potential empty strings gracefully.
    if case_sensitive:
        return [name for name in names if name and name.startswith('M')]
    else:
        # For case-insensitivity, convert the name to lowercase before checking.
        return [name for name in names if name and name.lower().startswith('m')]
