from src.db import test_connection
from src.analysis import (
    get_accounts,
    get_transactions,
    get_edges,
    detect_loops,
)

def main():
    loops = detect_loops()
    unique_loops = set()

    for loop in loops:
        cycle = [loop['a'], loop['b'], loop['c']]

        min_index = cycle.index(min(cycle))
        normalized = tuple(cycle[min_index:] + cycle[:min_index])
        unique_loops.add(normalized)
    
    print(f"Accounts: {get_accounts()}")
    print(f"Transactions: {get_transactions()}")
    print(f"Edges: {get_edges()}")
    print(f"Loops: {loops}")
    print('------------------------')
    print('The following fraud patterns were detected:')
    for a, b, c in unique_loops:
        print(f" - Loop detected: {a} -> {b} -> {c} -> {a}")

if __name__ == "__main__":
    test_connection()
    main()