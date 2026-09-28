#28
n = 98765
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print("Digit count:", count)


#29
n = 121
original = n
rev = 0
while n > 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#30
a = 48
b = 18
while b != 0:
    a, b = b, a % b
print("GCD:", a)


#31
n = 6
length = 1
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    length += 1
print("Collatz length:", length)


#32
n = 13
binary_str = ""
if n == 0:
    binary_str = "0"
while n > 0:
    binary_str = str(n % 2) + binary_str
    n //= 10
print("Binary:", binary_str)


#33
n = 25.0
x = n
while True:
    root = 0.5 * (x + (n / x))
    if abs(root - x) < 0.00001:
        break
    x = root
print("Square root:", root)



#34
a = 2
b = 10
res = 1
while b > 0:
    if b % 2 == 1:
        res *= a
    a *= a
    b //= 2
print("Result:", res)




#35
target = 42
guess = 0
while guess != target:
    guess = int(input("Enter your guess: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct!")


#36
total = 0
count = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num
    count += 1
print("Sum:", total)
if count > 0:
    print("Average:", total / count)

#37
n = 13  # 1101 in binary
count = 0
while n > 0:
    n = n & (n - 1)
    count += 1
print("Set bits:", count)


#38
k = 15
numbers = [3, 8, 2, 11, 4]
idx = 0
total = 0
while idx < len(numbers) and total <= k:
    total += numbers[idx]
    idx += 1
print("Final Total:", total)
print("Numbers added:", idx)


#39
n = 9875
while n >= 10:
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    n = digit_sum
print("Digital root:", n)


#40
principal = 1000.0
rate = 0.07  # 7% interest
balance = principal
years = 0
while balance < 2 * principal:
    balance += balance * rate
    years += 1
print("Years to double:", years)




#41
choice=2
while choice != 3:
    print("--- MENU ---")
    print("1. Play Game")
    print("2. Settings")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Starting game...\n")
    elif choice == 2:
        print("Opening settings...\n")
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice, try again.\n")


#42
n = 100
zeros = 0
divisor = 5
while n // divisor > 0:
    zeros += n // divisor
    divisor *= 5
print("Trailing zeros:", zeros)


#43
balance = 500
withdrawals = [100, 300, 200]
idx = 0
while idx < len(withdrawals):
    amount = withdrawals[idx]
    if amount > balance:
        print(f"Cannot withdraw {amount}. Insufficient balance ({balance}).")
    else:
        balance -= amount
        print(f"Withdrew {amount}. Remaining balance: {balance}")
    idx += 1



#44
nums = [12, 45, 2, 89, 34]
total = 0
maximum = nums[0]
minimum = nums[0]
for x in nums:
    total += x
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
print("Sum:", total)
print("Max:", maximum)
print("Min:", minimum)



#45
text = "Hello World"
vowels = 0
consonants = 0
for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)


#46
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
print("Reversed list:", arr)



#47
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



#48
n = 28
print(f"Factors of {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()



#49
n = 29
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} is Prime")
else:
    print(f"{n} is Not Prime")



#50
n = 10
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)



#51
sentence = "apple banana apple cherry banana apple"
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word frequencies:", freq)



#52
nums = [10, 40, 20, 50, 30]
first = float('-inf')
second = float('-inf')
for x in nums:
    if x > first:
        second = first
        first = x
    elif x > second and x != first:
        second = x
print("Second largest:", second)



#53
arr = [2, 7, 4, 3, 5, 1]
target = 8
print(f"Pairs summing to {target}:")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"({arr[i]}, {arr[j]})")



#54
terms = 7
a, b = 0, 1
print("Fibonacci series:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()



#56
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i

print(f"Factorial of {n}:", fact)



#56
n = 5
total = 0.0
for i in range(1, n + 1):
    total += 1 / i
print("Series sum:", round(total, 4))



#57
num = 12234252
target_digit = 2
count = 0
for ch in str(num):
    if ch == str(target_digit):
        count += 1
print(f"Digit {target_digit} appears {count} times.")



#58
start_code = 65  # 'A'
end_code = 70    # 'F'
for code in range(start_code, end_code + 1):
    print(f"ASCII {code} -> {chr(code)}")
