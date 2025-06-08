
from collections import defaultdict, deque
from typing import List

def alien_order(words: List[str]) -> str:
    """
    Determines the character order of an alien language from a sorted list of words.
    
    :param words: List of words sorted lexicographically in the alien language.
    :return: A string representing the characters in correct order. Returns empty string if invalid.
    """

    # Step 1: Initialize graph and in-degree count
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build the graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        # Check for prefix conflict (invalid case)
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""

        # Compare characters to find the first different character
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                if c2 not in graph[c1]:  # Prevent duplicate edges
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

    # Step 3: Topological Sort (Kahn’s algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result length != total unique chars, there's a cycle
    if len(result) != len(in_degree):
        return ""

    return ''.join(result)


def run_tests():
    """Runs test cases for the alien_order function."""

    print("=== TEST CASES ===")

    # Test Case 1: Normal alien dictionary
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Input:", words1)
    print("Expected Output: 'wertf'")
    print("Actual Output:", alien_order(words1))
    print()

    # Test Case 2: Another valid order
    words2 = ["z", "x", "z"]
    print("Input:", words2)
    print("Expected Output: '' (cycle)")
    print("Actual Output:", alien_order(words2))
    print()

    # Test Case 3: Single word
    words3 = ["abc"]
    print("Input:", words3)
    print("Expected Output: 'abc' (any order of unique letters is valid)")
    print("Actual Output:", alien_order(words3))
    print()

    # Test Case 4: Invalid prefix case
    words4 = ["abc", "ab"]
    print("Input:", words4)
    print("Expected Output: '' (invalid input)")
    print("Actual Output:", alien_order(words4))
    print()

    # Test Case 5: Minimal input
    words5 = ["a", "b"]
    print("Input:", words5)
    print("Expected Output: 'ab'")
    print("Actual Output:", alien_order(words5))
    print()


if __name__ == "__main__":
    run_tests()
