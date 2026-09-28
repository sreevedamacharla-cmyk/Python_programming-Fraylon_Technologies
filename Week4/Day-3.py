#59
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array (Bubble Sort):", arr)

#60
arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted array (Selection Sort):", arr)

#61
arr = [24, 60, 36, 84]

result = arr[0]

for i in range(1, len(arr)):
    b = arr[i]
    while b != 0:
        result, b = b, result % b

print("GCD of array:", result)

#62
n = 5

sum_numbers = sum(range(1, n + 1))
sum_squares = sum(i ** 2 for i in range(1, n + 1))
sum_cubes = sum(i ** 3 for i in range(1, n + 1))

print("Sum of numbers:", sum_numbers) # 1+2+3+4+5 = 15
print("Sum of squares:", sum_squares) # 1+4+9+16+25 = 55
print("Sum of cubes:", sum_cubes)     # 1+8+27+64+125 = 225

#63
start, stop = 1, 10

print("Even numbers:")
for i in range(2 if start % 2 != 0 else start, stop + 1, 2):
    print(i, end=" ")
print()

print("Odd numbers:")
for i in range(1 if start % 2 == 0 else start, stop + 1, 2):
    print(i, end=" ")
print()

#64
start = 3
stop = 20
step = 3

print(f"Series from {start} to {stop} stepping by {step}:")
for num in range(start, stop + 1, step):
    print(num, end=" ")
print()

#65
arr = [10, 25, 15, 30, 5]

print("Comparing elements backwards:")
for i in range(len(arr) - 1, 0, -1):
    current = arr[i]
    prev = arr[i - 1]
    print(f"Index {i} ({current}) vs Index {i-1} ({prev}) -> Diff: {current - prev}")

#66
n = 30
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

print(f"Primes up to {n}:")
for num in range(2, n + 1):
    if is_prime[num]:
        print(num, end=" ")
print()

#67
items = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

print(f"List split into chunks of size {k}:")
for i in range(0, len(items), k):
    chunk = items[i : i + k]
    print(chunk)

#68
n = 10
total = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(f"Sum of multiples of 3 or 5 below {n}:", total)


#69
n = 12
k = 3

print(f"Numbers 1 to {n} skipping multiples of {k}:")
for i in range(1, n + 1):
    if i % k == 0:
        continue
    print(i, end=" ")
print()


#70
a, d, terms = 2, 3, 5  # AP: start=2, diff=3

print("Arithmetic Progression (AP):")
for term in range(a, a + terms * d, d):
    print(term, end=" ")
print()

a, r, terms = 2, 3, 5  # GP: start=2, ratio=3
print("Geometric Progression (GP):")
current_gp = a
for _ in range(terms):
    print(current_gp, end=" ")
    current_gp *= r
print()

#71
n = 5

for i in range(n, -1, -1):
    if i == 0:
        print("0 -> Liftoff!")
    else:
        print(f"{i}...")

#72
rows, cols = 3, 3

grid_indices = []
for r in range(rows):
    for c in range(cols):
        grid_indices.append((r, c))

print("Grid coordinates (Row, Column):")
print(grid_indices)

#73
start, stop, step = 1, 10, 2  
offset = 5                   

total = 0
for x in range(start, stop, step):
    total += (x + offset)

print("Sum with offset applied:", total)



#74
n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  

#75
n = 5

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#76
n = 5

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

#77
n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

#78


for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


#79
n = 4
num = 1

for i in range(n):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()



#80
n = 5

for i in range(n):
    # Print leading spaces for pyramid alignment
    print(" " * (n - i - 1), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()

#81
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#82
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for r in range(len(A)):
    for c in range(len(A[0])):
        result[r][c] = A[r][c] + B[r][c]

print("Matrix Sum:", result)
#83
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix Product:", result)

#84
matrix = [[1, 2, 3], [4, 5, 6]]

rows = len(matrix)
cols = len(matrix[0])

# Initialize empty transpose matrix of size cols x rows
transposed = []
for c in range(cols):
    row = []
    for r in range(rows):
        row.append(matrix[r][c])
    transposed.append(row)

print("Transposed Matrix:", transposed)

#85
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

is_symmetric = True
n = len(matrix)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

print("Is Symmetric:", is_symmetric)

#86
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
main_diag = 0
anti_diag = 0

for i in range(n):
    main_diag += matrix[i][i]
    anti_diag += matrix[i][n - 1 - i]

print("Main Diagonal Sum:", main_diag) # 1 + 5 + 9 = 15
print("Anti Diagonal Sum:", anti_diag) # 3 + 5 + 7 = 15

#87
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = []

for row in matrix:
    for item in row:
        flat.append(item)

print("Flattened List:", flat)

#88
nums = [1, 3, 4, 2, 2, 5, 3]
duplicates = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and nums[i] not in duplicates:
            duplicates.append(nums[i])

print("Duplicates found:", duplicates)

#89
for num in range(1, 6):
    print(f"--- Table for {num} ---")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()

#90
nums = [2, 4, 3, 6, 5]
target_product = 12

found_pair = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] == target_product:
            print(f"Pair found: ({nums[i]}, {nums[j]})")
            found_pair = True

if not found_pair:
    print("No pair found.")

#91
def solid_rectangle(rows, cols):
    for i in range(rows):
        print("*" * cols)

#92
def hollow_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


#93
def four_corners_triangle(n):
    # Top-Left
    for i in range(1, n + 1):
        print("*" * i)
    print()
    # Top-Right
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    print()
    # Bottom-Left
    for i in range(n, 0, -1):
        print("*" * i)
    print()
    # Bottom-Right
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

#94
def inverted_hollow_right_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#95
def hollow_inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if i == n or j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#96
def hollow_diamond_in_box(n):
    # Top half
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    # Bottom half
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

#97
def half_diamond(n):
    # Right-facing
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)

#98
def downward_triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

#99
def sandglass_numbers(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))
    for i in range(2, n + 1):
        print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))

#100
def butterfly_numbers(n):
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i, 0, -1))
        print(left.ljust(n) + right.rjust(n))
    for i in range(n, 0, -1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i, 0, -1))
        print(left.ljust(n) + right.rjust(n))
