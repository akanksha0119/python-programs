
from typing import List, Tuple

def is_valid_block(block: List[str]) -> bool:
    """Check if a block of 9 cells contains digits 1–9 without repetition."""
    seen = set()
    for cell in block:
        if cell == ".":
            continue
        if cell in seen:
            return False
        seen.add(cell)
    return True


def is_valid_sudoku(board: List[List[str]], custom_zones: List[List[Tuple[int, int]]] = []) -> bool:
    """
    Validates the Sudoku board:
    - Rows
    - Columns
    - 3x3 boxes
    - Custom zones (if provided)
    """
    # Check rows
    for row in board:
        if not is_valid_block(row):
            return False

    # Check columns
    for col in range(9):
        if not is_valid_block([board[row][col] for row in range(9)]):
            return False

    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row+3) for c in range(box_col, box_col+3)]
            if not is_valid_block(box):
                return False

    # Check custom zones
    for zone in custom_zones:
        block = [board[r][c] for r, c in zone]
        if not is_valid_block(block):
            return False

    return True


def run_tests():
    """Runs predefined test cases with sample input/output"""

    print("=== TEST CASES ===")

    # Sample valid board
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

    # Valid custom zones
    custom_zones_valid = [
        [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (4,0)],
        [(0,2), (0,3), (1,2), (1,3), (2,2), (2,3), (3,2), (3,3), (4,2)],
    ]

    print("Test Case 1 - Valid board with valid custom zones:")
    print("Expected Output: True")
    print("Actual Output:", is_valid_sudoku(sample_board, custom_zones_valid))
    print()

    # Invalid custom zone with duplicate '8'
    custom_zones_invalid = [
        [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (2,2)]  # duplicate '8'
    ]

    print("Test Case 2 - Invalid custom zone with duplicate '8':")
    print("Expected Output: False")
    print("Actual Output:", is_valid_sudoku(sample_board, custom_zones_invalid))
    print()

    # Invalid due to duplicate in row
    board_with_row_error = [row.copy() for row in sample_board]
    board_with_row_error[0][1] = "5"  # duplicate '5' in row 0

    print("Test Case 3 - Invalid board with duplicate in a row:")
    print("Expected Output: False")
    print("Actual Output:", is_valid_sudoku(board_with_row_error))
    print()

    # Invalid due to duplicate in column
    board_with_col_error = [row.copy() for row in sample_board]
    board_with_col_error[1][0] = "5"  # duplicate '5' in column 0

    print("Test Case 4 - Invalid board with duplicate in a column:")
    print("Expected Output: False")
    print("Actual Output:", is_valid_sudoku(board_with_col_error))
    print()


if __name__ == "__main__":
    run_tests()
