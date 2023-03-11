
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
n = 99999999999


sequence = collatz_sequence(n)
print(f"The Collatz sequence for {n} is: {sequence}")
print(f"The number of iterations are:{len(sequence)}")
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,len(sequence))
y=np.array(sequence)
plt.title("Histogram")
plt.xlabel("No of iterations")
plt.ylabel("Collatz Sequence")
plt.plot(x,y,color="red")
plt.show()
