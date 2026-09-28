#101
def hollow_butterfly(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n + 1):
            if j == 1 or j == i or j == 2 * n or j == 2 * n - i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n, 0, -1):
        for j in range(1, 2 * n + 1):
            if j == 1 or j == i or j == 2 * n or j == 2 * n - i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#102
def continuous_number_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

#103
def right_aligned_number_triangle(n):
    for i in range(1, n + 1):
        nums = "".join(str(x) for x in range(1, i + 1))
        print(nums.rjust(n))

#104
def same_digit_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + (str(i) + " ") * i)

#105
def consecutive_num_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        row = " ".join(str(num + j) for j in range(i))
        print(" " * (n - i) + row)
        num += i

#106
def odd_num_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(num))
            num += 2
        print(" " * (n - i) + " ".join(row))

#107
def binary_triangle_start_one(n):
    for i in range(1, n + 1):
        val = 1
        for j in range(i):
            print(val, end="")
            val = 1 - val
        print()

#108
def binary_checkerboard(n):
    for i in range(n):
        for j in range(n):
            print((i + j) % 2, end=" ")
        print()

#109
def alphabet_floyd(n):
    ch = 65
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ch), end=" ")
            ch += 1
        print()

#110
def alphabet_inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

#111
def alphabet_same_letter_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + (chr(64 + i) + " ") * i)

#112
def continuous_alphabet_pattern(n):
    ch = 65
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ch), end="")
            ch += 1
        print()

#113
def palindromic_alphabet_pyramid(n):
    for i in range(1, n + 1):
        left = "".join(chr(64 + x) for x in range(1, i + 1))
        right = "".join(chr(64 + x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)

#114
def digit_diamond(n):
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)
    for i in range(n - 1, 0, -1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)

#115
def zigzag_pattern(n):
    for i in range(1, 4):
        for j in range(1, n + 1):
            if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()

#116
def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    for row in matrix:
        print(*row)

#117
def arrow_pattern(n):
    for i in range(1, n + 1):
        print(" " * (2 * (i - 1)) + "*")
    for i in range(n - 1, 0, -1):
        print(" " * (2 * (i - 1)) + "*")

#118
def heart_pattern(n=6):
    for i in range(n // 2, n, 2):
        print(" " * ((n - i) // 2) + "*" * i + " " * (n - i) + "*" * i)
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

#119
def pyramid_hollow_inside(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#120
def k_shape(n):
    for i in range(n, 0, -1):
        print("*" * i)
    for i in range(2, n + 1):
        print("*" * i)

#121
def hollow_cross(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#122
def plus_hollow_center(n):
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if (i == mid or j == mid) and not (i == mid and j == mid):
                print("*", end="")
            else:
                print(" ", end="")
        print()

#123
def sierpinski_pascal(n):
    for i in range(n):
        num = 1
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print("*" if num % 2 != 0 else " ", end=" ")
            num = num * (i - j) // (j + 1)
        print()

#124
def number_spiral_grid(n):
    for i in range(n):
        for j in range(n):
            print(max(abs(i - n // 2), abs(j - n // 2)) + 1, end=" ")
        print()

#125
def rhombus_stars(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * n)


#126
def christmas_tree(n):
    for t in range(1, 4):
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
    # Trunk
    for _ in range(2):
        print(" " * (n - 2) + "|||")

#127
def hollow_in_solid_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == n or i == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#128
def number_x_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i or j == n - i + 1:
                print(i, end="")
            else:
                print(" ", end="")
        print()

#129
def alphabet_diamond(n):
    for i in range(1, n + 1):
        left = "".join(chr(64 + x) for x in range(1, i + 1))
        right = "".join(chr(64 + x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)
    for i in range(n - 1, 0, -1):
        left = "".join(chr(64 + x) for x in range(1, i + 1))
        right = "".join(chr(64 + x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)

#130
def right_pascal_stars(n):
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)

#131
def left_pascal_stars(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * i)

#132
def border_ones_inside_zeros(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print(1, end="")
            else:
                print(0, end="")
        print()

#133
def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

#134
def row_value_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + (str(i) + " ") * i)

#135
def hollow_parallelogram(n):
    for i in range(n):
        print(" " * (n - 1 - i), end="")
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#136
def digit_diamond_fixed(n, digit):
    for i in range(1, n + 1):
        print(" " * (n - i) + (str(digit) + " ") * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + (str(digit) + " ") * i)

#137
def countdown_row_triangle(n):
    for i in range(n, 0, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()

#138
def mirror_floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        row = " ".join(str(num + j) for j in range(i))
        print(row.rjust(20))
        num += i

#139
def number_wave(wave_len):
    for i in range(1, 4):
        for j in range(1, wave_len + 1):
            if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()

#140
def concentric_square_rings(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            dist = min(i, j, size - 1 - i, size - 1 - j)
            print(n - dist, end=" ")
        print()

#141
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 142]
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors

# 143
def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, n + 1, i):
                is_p[j] = False
    return [i for i in range(n + 1) if is_p[i]]

# 144
def is_armstrong(n):
    s = str(n)
    p = len(s)
    return sum(int(d)**p for d in s) == n

# 145
def is_perfect(n):
    if n <= 1: return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# 146
import math
def is_strong(n):
    return sum(math.factorial(int(d)) for d in str(n)) == n

# 147
def is_harshad(n):
    s = sum(int(d) for d in str(n))
    return n % s == 0

# 148
def is_automorphic(n):
    return str(n**2).endswith(str(n))

# 149
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

# 150
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
