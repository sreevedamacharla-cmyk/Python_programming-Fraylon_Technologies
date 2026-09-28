# 151
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# 152
def gcd_lcm(a, b):
    x, y = a, b
    while y:
        x, y = y, x % y
    return x, (a * b) // x

# 153
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

# 154
def reverse_number(n):
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev if n >= 0 else -rev

# 155
def count_and_sum_digits(n):
    cnt = 0
    even_sum, odd_sum = 0, 0
    for d in str(abs(n)):
        cnt += 1
        val = int(d)
        if val % 2 == 0: even_sum += val
        else: odd_sum += val
    return cnt, even_sum, odd_sum

# 156
def power(a, b):
    res = 1
    for _ in range(b):
        res *= a
    return res

# 157
def sum_series(n):
    sum_n = sum(range(1, n + 1))
    sum_sq = sum(i**2 for i in range(1, n + 1))
    return sum_n, sum_sq

# 158
def alternating_series(n):
    return sum(i if i % 2 != 0 else -i for i in range(1, n + 1))

# 159
def number_to_words(n):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return " ".join(words[int(d)] for d in str(n))

# 160
def convert_base(n):
    return bin(n)[2:], oct(n)[2:], hex(n)[2:]

# 161
def trailing_zeros_factorial(n):
    count = 0
    while n >= 5:
        count += n // 5
        n //= 5
    return count

# 162
def nth_ap_gp(a, d, r, n):
    nth_ap = a + (n - 1) * d
    nth_gp = a * (r ** (n - 1))
    return nth_ap, nth_gp

# 163
def sum_odd_even(n):
    sum_odd = sum(2 * i + 1 for i in range(n))
    sum_even = sum(2 * i for i in range(1, n + 1))
    return sum_odd, sum_even

# 164
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0: n //= 2
        else: n = 3 * n + 1
        steps += 1
    return steps

# 165
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


# 166
def classify_chars(s):
    v = c = d = sp = 0
    for ch in s:
        if ch.isdigit(): d += 1
        elif ch.isspace(): sp += 1
        elif ch.lower() in "aeiou": v += 1
        elif ch.isalpha(): c += 1
    return v, c, d, sp

# 167
def reverse_string(s):
    res = ""
    for ch in s:
        res = ch + res
    return res

# 168
def is_palindrome_str(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

# 169
def toggle_case(s):
    res = []
    for ch in s:
        if 'a' <= ch <= 'z': res.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z': res.append(chr(ord(ch) + 32))
        else: res.append(ch)
    return "".join(res)

# 170
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 171
def first_non_repeating(s):
    freq = char_frequency(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
