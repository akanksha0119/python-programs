"""
Sudoku Validator With Custom Zones
----------------------------------
This script validates a 9x9 Sudoku board with the following rules:
1. Each row must contain digits 1–9 without repetition.
2. Each column must contain digits 1–9 without repetition.
3. Each 3x3 standard subgrid must contain digits 1–9 without repetition.
4. Each custom zone (9 cells specified manually) must contain digits 1–9 without repetition.

Empty cells are represented with '.'
"""

from typing import List, Tuple

def is_valid_group(group: List[str]) -> bool:
    """
    Checks whether a group (row/column/box/custom zone) has unique digits from 1–9.
    Ignores empty cells represented by '.'.
    """
    digits = [cell for cell in group if cell != '.']
    return len(digits) == len(set(digits))

def validate_rows(board: List[List[str]]) -> bool:
    for row in board:
        if not is_valid_group(row):
            return False
    return True

def validate_columns(board: List[List[str]]) -> bool:
    for col in zip(*board):
        if not is_valid_group(col):
            return False
    return True

def validate_subgrids(board: List[List[str]]) -> bool:
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            block = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_group(block):
                return False
    return True

def validate_custom_zones(board: List[List[str]], custom_zones: List[List[Tuple[int, int]]]) -> bool:
    for zone in custom_zones:
        if len(zone) != 9:
            raise ValueError("Each custom zone must have exactly 9 cells.")
        cells = [board[r][c] for r, c in zone]
        if not is_valid_group(cells):
            return False
    return True

def is_valid_sudoku(board: List[List[str]], custom_zones: List[List[Tuple[int, int]]]) -> bool:
    """
    Validates the entire Sudoku board with custom zones.
    """
    return (
        validate_rows(board)
        and validate_columns(board)
        and validate_subgrids(board)
        and validate_custom_zones(board, custom_zones)
    )

# ------------------- TEST CASES -------------------

def run_tests():
    sample_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    custom_zones = [
        [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (4,0)],  # Should be valid
        [(0,2), (0,3), (1,2), (1,3), (2,2), (2,3), (3,2), (3,3), (4,2)]   # Should be valid
    ]

    print("=== TEST CASES ===")
    print("Test Case 1 - Valid board with valid custom zones:")
    print("Expected Output: True")
    print("Actual Output:", is_valid_sudoku(sample_board, custom_zones))

    # Invalid custom zone with duplicate '8'
    custom_zones_invalid = [
        [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (2,2)]  # '8' appears twice
    ]
    print("\nTest Case 2 - Invalid custom zone with duplicate '8':")
    print("Expected Output: False")
    print("Actual Output:", is_valid_sudoku(sample_board, custom_zones_invalid))

if __name__ == "__main__":
    run_tests()
