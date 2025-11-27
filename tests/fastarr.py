"""
High-Performance Array Implementation in Codon
Demonstrates Codon's speed with efficient array operations
"""

class FastArray:
    """A fast dynamic array implementation optimized for Codon"""
    data: Ptr[int]
    size: int
    capacity: int
    
    def __init__(self, initial_capacity: int = 16):
        self.size = 0
        self.capacity = initial_capacity
        self.data = Ptr[int](initial_capacity)
    
    def __len__(self) -> int:
        return self.size
    
    def _resize(self, new_capacity: int):
        """Double the capacity when needed"""
        new_data = Ptr[int](new_capacity)
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def append(self, value: int):
        """Add element to end of array"""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1
    
    def get(self, index: int) -> int:
        """Get element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def set(self, index: int, value: int):
        """Set element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value
    
    def sum(self) -> int:
        """Fast sum of all elements"""
        total = 0
        for i in range(self.size):
            total += self.data[i]
        return total
    
    def map_multiply(self, factor: int):
        """Multiply all elements by factor in-place"""
        for i in range(self.size):
            self.data[i] *= factor
    
    def filter_greater(self, threshold: int) -> FastArray:
        """Return new array with elements > threshold"""
        result = FastArray(self.size)
        for i in range(self.size):
            if self.data[i] > threshold:
                result.append(self.data[i])
        return result


def benchmark_operations():
    """Benchmark various array operations"""
    import time
    
    # Create array with 10 million elements
    n = 10_000_000
    arr = FastArray(n)
    
    # Benchmark append
    start = time.time()
    for i in range(n):
        arr.append(i)
    append_time = time.time() - start
    
    # Benchmark sum
    start = time.time()
    total = arr.sum()
    sum_time = time.time() - start
    
    # Benchmark map operation
    start = time.time()
    arr.map_multiply(2)
    map_time = time.time() - start
    
    # Benchmark filter
    start = time.time()
    filtered = arr.filter_greater(n // 2)
    filter_time = time.time() - start
    
    print(f"FastArray Performance Benchmark (n={n:,})")
    print(f"{'='*50}")
    print(f"Append {n:,} elements: {append_time:.4f}s")
    print(f"Sum all elements:      {sum_time:.4f}s")
    print(f"Map multiply by 2:     {map_time:.4f}s")
    print(f"Filter > {n//2:,}:       {filter_time:.4f}s")
    print(f"\nTotal sum: {total:,}")
    print(f"Filtered size: {len(filtered):,}")


def demo_usage():
    """Demonstrate basic array usage"""
    print("FastArray Demo")
    print("="*50)
    
    # Create and populate array
    arr = FastArray()
    for i in range(10):
        arr.append(i * 10)
    
    print(f"Array size: {len(arr)}")
    print(f"Elements: ", end="")
    for i in range(len(arr)):
        print(arr.get(i), end=" ")
    print()
    
    # Sum elements
    print(f"Sum: {arr.sum()}")
    
    # Multiply all by 2
    arr.map_multiply(2)
    print(f"After multiplying by 2:")
    for i in range(len(arr)):
        print(arr.get(i), end=" ")
    print()
    
    # Filter
    filtered = arr.filter_greater(50)
    print(f"\nFiltered (>50): ", end="")
    for i in range(len(filtered)):
        print(filtered.get(i), end=" ")
    print()


if __name__ == "__main__":
    demo_usage()
    print("\n")
    benchmark_operations()
