from typing import List, Union, Tuple

def select_names_starting_with(
    names: List[str],
    prefix: Union[str, Tuple[str, ...]],
    case_sensitive: bool = False
) -> List[str]:

    if not isinstance(prefix, (str, tuple)):
        raise TypeError("Prefix must be a string or a tuple of strings.")
    if isinstance(prefix, tuple) and not all(isinstance(p, str) for p in prefix):
        raise TypeError("All elements in the prefix tuple must be strings.")

    filtered_names = []
    for name in names:
        if not isinstance(name, str) or not name:
            continue 

        if case_sensitive:
            if name.startswith(prefix):
                filtered_names.append(name)
        else:
            name_lower = name.lower()
            if isinstance(prefix, str):
                if name_lower.startswith(prefix.lower()):
                    filtered_names.append(name)
            elif isinstance(prefix, tuple):
                lower_prefixes = tuple(p.lower() for p in prefix)
                if name_lower.startswith(lower_prefixes):
                    filtered_names.append(name)
    return filtered_names

def select_names_starting_with_M(names: List[str], case_sensitive: bool = False) -> List[str]:
    return select_names_starting_with(names, 'M', case_sensitive)
