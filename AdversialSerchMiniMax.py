import math

def minimax(depth, node_index, is_maximizing, scores, height):
    
    # Base case: if leaf node is reached
    if depth == height:
        return scores[node_index]

    # If current player is Maximizer
    if is_maximizing:
        left = minimax(depth + 1, node_index * 2, False, scores, height)
        right = minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        return max(left, right)

    # If current player is Minimizer
    else:
        left = minimax(depth + 1, node_index * 2, True, scores, height)
        right = minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        return min(left, right)

def compute_height(num_leaves):
    # Returns the height (depth) of the binary tree.
    return int(math.log2(num_leaves))

def main():
    print("\nAdversarial Search using Mini–Max Algorithm \n")

    try:
        # Step 1: Take user input for leaf node values
        scores = list(map(int, input("Enter the leaf node values separated by spaces: ").split()))
        n = len(scores)

        # Step 2: Validate that number of leaves is a power of 2
        if math.log2(n) % 1 != 0:
            print("\nError: Number of leaf nodes must be a power of 2 (e.g., 2, 4, 8, 16...).")
            return

        # Step 3: Calculate tree height
        height = compute_height(n)

        # Step 4: Display information
        print(f"\nNumber of leaf nodes: {n}")
        print(f"Tree height: {height}")
        print(f"Leaf node values: {scores}")

        # Step 5: Compute the optimal value using Mini–Max
        optimal_value = minimax(0, 0, True, scores, height)

        # Step 6: Display the result
        print("\nOptimal value determined by Mini–Max Algorithm:", optimal_value)

    except ValueError:
        print("\nInvalid input! Please enter numeric leaf node values separated by spaces.")

if __name__ == "__main__":
    main()

# Adversarial Search using Mini–Max Algorithm

# Enter the leaf node values separated by spaces: 2 5 1 9

# Number of leaf nodes: 4
# Tree height: 2
# Leaf node values: [2, 5, 1, 9]

# Optimal value determined by Mini–Max Algorithm: 2

    #            (MAX)
    #          /       \
    #      (MIN)        (MIN)
    #     /     \      /     \
    #   2       5    1       9
