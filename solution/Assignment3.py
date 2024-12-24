def fibonacci_1(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Test
n_terms = 10
print(f"Fibonacci sequence with {n_terms} terms: {fibonacci_1(n_terms)}")
