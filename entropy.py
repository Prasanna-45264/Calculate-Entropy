import math
from collections import Counter

def calculate_entropy(file_path):
    """
    Calculate Shannon Entropy of a file.

    :param file_path: Path to the file
    :return: Entropy value (float)
    """

    with open(file_path, 'rb') as f:
        data = f.read()

    if not data:
        return 0.0

    byte_counts = Counter(data)
    file_size = len(data)

    entropy = 0.0
    for count in byte_counts.values():
        probability = count / file_size
        entropy -= probability * math.log2(probability)

    return entropy


# Example usage
if __name__ == "__main__":
    path = input("Enter file path: ")
    entropy_value = calculate_entropy(path)
    print(f"Shannon Entropy: {entropy_value:.4f} bits per byte")
