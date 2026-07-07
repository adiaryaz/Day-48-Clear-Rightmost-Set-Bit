# Day-48-Clear-Rightmost-Set-Bit

Day 48/100 - Python Program To Clear Rightmost Set Bit of a Number

# Clear Rightmost Set Bit of a Number

A program to strategically turn off (clear) the lowest-order `1` bit in the binary representation of an integer using an $O(1)$ bitwise operation.

## 📝 Description

This program modifies a user-inputted integer by finding its rightmost "set bit" (a bit carrying the value of `1`) and changing it to `0`, leaving all other bits completely unchanged.

Instead of converting the number to a string and searching for the character, it utilizes a highly efficient mathematical bitwise trick: `n & (n - 1)`.
When you subtract 1 from any binary number, it flips all the bits up to and including the rightmost `1`. By performing a bitwise AND (`&`) operation between the original number `n` and `n - 1`, that specific rightmost `1` safely cancels out to `0`. The script also uses Python's built-in `bin()` function to display the before-and-after binary representations clearly in the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer value (preferably non-negative).

### Output:

* Two formatted strings:
1. "Original number: [num] (Binary: [binary_num])"
2. "Number after clearing rightmost set bit: [result] (Binary: [binary_result])"



### Rules:

1. The program must accept an integer input from the user.
2. The core logic must be executed inside a function named `clear_rightmost_set_bit(n)`.
3. The function must return the result of the bitwise operation `n & (n - 1)`.
4. The program must print both the decimal and binary values of the original number and the resulting number.

---

## 💡 Examples

### Example 1 (Standard Integer)

**Input:**

```
12

```

**Output:**

```
Original number: 12 (Binary: 0b1100)
Number after clearing rightmost set bit: 8 (Binary: 0b1000)

```

**Explanation:** In binary, 12 is `1100`. The rightmost `1` is in the "fours" position ($2^2$). Subtracting 1 gives 11 (`1011`). `1100 & 1011` results in `1000`, which is the decimal number 8.

### Example 2 (Consecutive Set Bits)

**Input:**

```
7

```

**Output:**

```
Original number: 7 (Binary: 0b111)
Number after clearing rightmost set bit: 6 (Binary: 0b110)

```

**Explanation:** In binary, 7 is `111`. The rightmost `1` is in the "ones" position ($2^0$). Clearing it leaves `110`, which is the decimal number 6.

### Example 3 (Perfect Power of Two)

**Input:**

```
16

```

**Output:**

```
Original number: 16 (Binary: 0b10000)
Number after clearing rightmost set bit: 0 (Binary: 0b0)

```

**Explanation:** A perfect power of two only has a single set bit. 16 is `10000`. Clearing that single bit leaves `00000`, returning the integer 0. (This is exactly why `n & (n - 1) == 0` is used to check for powers of two, as seen in Day 26!).

### Example 4 (Zero Edge Case)

**Input:**

```
0

```

**Output:**

```
Original number: 0 (Binary: 0b0)
Number after clearing rightmost set bit: 0 (Binary: 0b0)

```

**Explanation:** The binary representation is `0`. Subtracting 1 gives -1. `0 & -1` mathematically evaluates back to `0`. No set bits existed to be cleared.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 48.py").

```bash
git clone https://github.com/adiaryaz/Day-48-Clear-Rightmost-Set-Bit.git
cd clear-rightmost-set-bit

```

2. **Run the program**:

```bash
python "Day 48.py"

```

Enter a non-negative integer when prompted to see its rightmost active bit mathematically erased.
