def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

# Example usage
#Enter the number you want
n = 5

sequence = collatz_sequence(n)
print(f"The Collatz sequence for {n} is: {sequence}")
print(f"The number of iterations are:{len(sequence)}")
