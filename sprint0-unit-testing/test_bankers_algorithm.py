"""Sprint 0 unit-testing exercise: pytest tests for bankers_algorithm.py,
a Banker's algorithm (deadlock avoidance) implementation. This demonstrates the pytest workflow chosen for the
Peg Solitaire project works"""

from bankers_algorithm import (
    bankers_algorithm,
    calculate_need_matrix
)

# Test that the calculate_need_matrix function works correctly
def test_calculate_need_matrix_subtracts_allocation_from_max():
    allocation = [[0, 1, 0], [2, 0, 0]]
    max_need = [[7, 5, 3], [3, 2, 2]]

    need = calculate_need_matrix(allocation, max_need)

    assert need == [[7, 4, 3], [1, 2, 2]]

# Tests that the bankers_algorithm function works correctly
def test_bankers_algorithm_finds_safe_sequence_for_classic_example():
    processes = ["P1", "P2", "P3", "P4", "P5"]
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    available = [3, 3, 2]

    safe, sequence = bankers_algorithm(processes, allocation, max_need, available)

    assert safe is True
    assert sequence == ["P2", "P4", "P1", "P3", "P5"]

