from name_filters import select_names_starting_with, select_names_starting_with_M

def run_examples():
    all_names = [
        "Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code",
        "mouse", "Maverick", "april", "November", "Monday", "", "Apple", "orange"
    ]

    print("Original list of names:", all_names)
    print("-" * 30)

    filtered_ci_m = select_names_starting_with_M(all_names)
    print("1. Selected (Case-Insensitive 'M'/'m' using wrapper):", filtered_ci_m)

    print("-" * 30)

    filtered_a = select_names_starting_with(all_names, 'A')
    print("2. Selected (Case-Insensitive 'A'/'a'):", filtered_a)

    print("-" * 30)

    filtered_nov_cs = select_names_starting_with(all_names, 'Nov', case_sensitive=True)
    print("3. Selected (Case-Sensitive 'Nov'):", filtered_nov_cs)

    print("-" * 30)

    filtered_b_or_c = select_names_starting_with(all_names, ('B', 'C'))
    print("4. Selected (Case-Insensitive 'B'/'b' or 'C'/'c'):", filtered_b_or_c)

    print("-" * 30)

    filtered_ma = select_names_starting_with(all_names, 'Ma')
    print("5. Selected (Case-Insensitive 'Ma'/'ma'):", filtered_ma)

    print("-" * 30)

    empty_list = []
    filtered_empty = select_names_starting_with(empty_list, 'X')
    print("6. Selected from empty list:", filtered_empty)

    print("-" * 30)

    try:
        select_names_starting_with(all_names, 123)
    except TypeError as e:
        print(f"7. Caught expected error for invalid prefix type: {e}")

    try:
        select_names_starting_with(all_names, ('M', 123))
    except TypeError as e:
        print(f"8. Caught expected error for invalid prefix tuple element: {e}")

if __name__ == "__main__":
    run_examples()
