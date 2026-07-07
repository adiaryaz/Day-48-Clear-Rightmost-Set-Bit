def clear_rightmost_set_bit(n):

    """
    Clears the rightmost set bit of the given number.
    : param n: The input number
    :return: The number with the rightmost set bit cleared
    """
    return n & (n - 1)

num = int(input("Enter a non-negative integer: "))
result = clear_rightmost_set_bit(num)

print(f"Original number: {num} (Binary: {bin(num)})")
print(f"Number after clearing rightmost set bit: {result} (Binary: {bin(result)})")