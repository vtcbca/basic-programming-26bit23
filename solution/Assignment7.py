def triangle_pattern_1(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print the numbers
        for j in range(1, 2 * i):
            print(j, end=" ")
        print()  # Move to the next line

# Test
n = 3
triangle_pattern_1(n)
