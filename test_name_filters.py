from select_m_names import select_names_starting_with_M

def run_examples():
    all_names = [
        "Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code", "mouse", "Maverick"
    ]

    print("Original list of names:", all_names)
    print("-" * 30)

    filtered_ci = select_names_starting_with_M(all_names)
    print("Selected (Case-Insensitive 'M'/'m'):", filtered_ci)

    print("-" * 30)

    filtered_cs = select_names_starting_with_M(all_names, case_sensitive=True)
    print("Selected (Case-Sensitive 'M'):", filtered_cs)

    print("-" * 30)

    empty_list = []
    filtered_empty = select_names_starting_with_M(empty_list)
    print("Selected from empty list:", filtered_empty)

    print("-" * 30)

    non_matching_list = ["apple", "banana", "cherry"]
    filtered_non_matching = select_names_starting_with_M(non_matching_list)
    print("Selected from non-matching list:", filtered_non_matching)

if __name__ == "__main__":
    run_examples()
