def alphabet_pattern_1(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Print increasing part of the row
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")

        # Print decreasing part of the row (excluding the middle element)
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")
        
        # Move to the next line
        print()

# Test
n = 3
alphabet_pattern_1(n)
