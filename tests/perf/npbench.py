#!/usr/bin/env python3
import numpy as np
import time

def benchmark(func, *args, repeat=5, **kwargs):
    """Run a function multiple times and report average execution time."""
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times), np.std(times)

def main():
    N = 10_000_000
    M = 2000

    print("NumPy Benchmark Results")
    print("=" * 40)

    # Array creation
    mean, std = benchmark(np.arange, N)
    print(f"Array creation (arange {N}): {mean:.6f}s ± {std:.6f}")

    # Element-wise addition
    a = np.random.rand(N)
    b = np.random.rand(N)
    mean, std = benchmark(lambda x, y: x + y, a, b)
    print(f"Element-wise addition ({N} elements): {mean:.6f}s ± {std:.6f}")

    # Element-wise multiplication
    mean, std = benchmark(lambda x, y: x * y, a, b)
    print(f"Element-wise multiplication ({N} elements): {mean:.6f}s ± {std:.6f}")

    # Reduction (sum)
    mean, std = benchmark(np.sum, a)
    print(f"Reduction sum ({N} elements): {mean:.6f}s ± {std:.6f}")

    # Matrix multiplication
    A = np.random.rand(M, M)
    B = np.random.rand(M, M)
    mean, std = benchmark(np.dot, A, B)
    print(f"Matrix multiplication ({M}x{M}): {mean:.6f}s ± {std:.6f}")

    # Broadcasting
    v = np.random.rand(M)
    mean, std = benchmark(lambda X, v: X + v, A, v)
    print(f"Broadcasting add (matrix {M}x{M} + vector {M}): {mean:.6f}s ± {std:.6f}")

if __name__ == "__main__":
    main()
