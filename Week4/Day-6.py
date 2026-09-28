# 172
def remove_duplicates(s):
    seen = set()
    res = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)

# 173
def count_words(s):
    return len(s.split())

# 174
def capitalise_words(s):
    return " ".join(word.capitalize() for word in s.split())

# 175
def is_anagram(s1, s2):
    return char_frequency(s1) == char_frequency(s2)

# 176
def longest_word(s):
    words = s.split()
    max_w = ""
    for w in words:
        if len(w) > len(max_w):
            max_w = w
    return max_w

# 177
def caesar_cipher(text, shift):
    res = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            res.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            res.append(ch)
    return "".join(res)

# 178
def count_substring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

# 179
def urlify(s):
    res = []
    for ch in s:
        res.append("%20" if ch == " " else ch)
    return "".join(res)

# 180
def all_unique(s):
    seen = set()
    for ch in s:
        if ch in seen: return False
        seen.add(ch)
    return True

# 181
def sum_ascii(s):
    total = 0
    for ch in s: total += ord(ch)
    return total

# 182
def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])

# 183
def compress_string(s):
    if not s: return ""
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(s[i - 1] + str(count))
            count = 1
    res.append(s[-1] + str(count))
    return "".join(res)


# 184
def print_matrix(mat):
    for row in mat:
        for val in row:
            print(val, end=" ")
        print()

# 185
def row_col_sums(mat):
    rows, cols = len(mat), len(mat[0])
    r_sums = [sum(row) for row in mat]
    c_sums = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]
    return r_sums, c_sums



# 186
def diagonal_sums(mat):
    n = len(mat)
    primary = sum(mat[i][i] for i in range(n))
    secondary = sum(mat[i][n - 1 - i] for i in range(n))
    return primary, secondary

# 187
def transpose(mat):
    r, c = len(mat), len(mat[0])
    return [[mat[j][i] for j in range(r)] for i in range(c)]

# 188
def add_subtract_matrices(A, B):
    r, c = len(A), len(A[0])
    add_mat = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]
    sub_mat = [[A[i][j] - B[i][j] for j in range(c)] for i in range(r)]
    return add_mat, sub_mat

# 189
def multiply_matrices(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])
    res = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] += A[i][k] * B[k][j]
    return res

# 190
def is_symmetric(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

# 191
def rotate_matrix_90(mat):
    transposed = transpose(mat)
    return [row[::-1] for row in transposed]

# 192
def spiral_order(mat):
    res = []
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1): res.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1): res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1): res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1): res.append(mat[i][left])
            left += 1
    return res

# 193
def border_elements(mat):
    r, c = len(mat), len(mat[0])
    res = []
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                res.append(mat[i][j])
    return res

# 194
def max_min_matrix(mat):
    max_val = float('-inf')
    min_val = float('inf')
    for row in mat:
        for val in row:
            if val > max_val: max_val = val
            if val < min_val: min_val = val
    return max_val, min_val

# 195
def saddle_point(mat):
    for i in range(len(mat)):
        min_in_row = min(mat[i])
        col_idx = mat[i].index(min_in_row)
        if all(mat[k][col_idx] <= min_in_row for k in range(len(mat))):
            return min_in_row, (i, col_idx)
    return None


#196

def hollow_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#197
def is_armstrong_mock(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

#198
def process_sentence(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in sentence if ch in vowels)
    reversed_words = " ".join(word[::-1] for word in sentence.split())
    return vowel_count, reversed_words

#199
def rotate_matrix_in_place(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse rows
    for i in range(n):
        matrix[i].reverse()
    return matrix

#200
def palindrome_number_pyramid(n):
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i - 1, 0, -1))
        print(" " * (n - i) + left + right)


#201
def print_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        is_p = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes