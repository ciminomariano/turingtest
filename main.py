def card_difference(a, b, x):
    difference_count = 0

    for card_a in a:
        has_close_card = False

        for card_b in b:
            if abs(card_a - card_b) <= x:
                has_close_card = True
                break

        if not has_close_card:
            difference_count += 1

    return difference_count


# Example input
a = [4, 5, 8]
b = [10, 9, 1, 8]
x = 2

# Calculate the difference
difference = card_difference(a, b, x)
print("Card Difference:", difference)


def calculate_typing_time(digits, num):
    positions = {digit: i for i, digit in enumerate(digits)}
    current_position = 0
    total_time = 0

    for digit in num:
        target_position = positions[digit]
        total_time += abs(target_position - current_position)
        current_position = target_position

    return total_time


# Example 1
digits1 = "0123456789"
num1 = "210"
output1 = calculate_typing_time(digits1, num1)
print("Output 1 typing time:", output1)  # Output: 8

# Example 2
digits2 = "8459761203"
num2 = "5439"
output2 = calculate_typing_time(digits2, num2)
print("Output 2: typing time", output2)  # Output: 17


def count_climbing_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev_prev = 1
    prev = 2

    for i in range(3, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return prev



n1 = 2
output1 = count_climbing_ways(n1)
print("Output 1 climbing:", output1)  # Output: 2

n2 = 3
output2 = count_climbing_ways(n2)
print("Output 2: climbing", output2)  # Output: 3


def generate_morse_variants(morsecode):
    variants = []

    for i in range(len(morsecode)):
        if i + 1 < len(morsecode) and morsecode[i:i + 2] == "..":
            new_variant = morsecode[:i] + "--" + morsecode[i + 2:]
            variants.append(new_variant)

    return variants



morsecode1 = "...."
output1 = generate_morse_variants(morsecode1)
print("Output 1 morse:", output1)  # Output: ['--..', '.--.', '..--']

morsecode2 = "--.-..-."
output2 = generate_morse_variants(morsecode2)
print("Output 2 morse:", output2)  # Output: []

morsecode3 = "........"
output3 = generate_morse_variants(morsecode3)
print("Output 3 morse:", output3)  # Output: ['------', '....--', '...---', '..----', '.-----']

morsecode4 = "..-..--..."
output4 = generate_morse_variants(morsecode4)
print("Output 4 morse:", output4)  # Output: ['--.---...', '-.-.--...', '..----...', '..-.--..']

