# personal_pattern_toolkit.py

# Task 1: Input Validation
def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number between 3 and 9: "))
            if 3 <= num <= 9:
                return num
            else:
                print("Invalid input. Please enter a number between 3 and 9.")
        except ValueError:
            print("Please enter a valid integer.")


# Task 2: Personal Code
def generate_personal_code(student_id, keyword):
    return f"{keyword[0].upper()}-{student_id}-{keyword[-1].upper()}"


# Task 3: Character Frequency
def count_character_frequency(name):
    freq = {}
    for ch in name.lower():
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq


# Task 4: Unique Vowels and Consonants
def find_unique_vowels_consonants(text):
    vowels = set("aeiou")
    unique_vowels = set()
    unique_consonants = set()

    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                unique_vowels.add(ch)
            else:
                unique_consonants.add(ch)

    return unique_vowels, unique_consonants


# Task 5: Stack-Based Bracket Checker
def check_balanced_brackets(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# Task 6: Queue Processing
def process_keyword_queue(keyword):
    queue = []
    for ch in keyword:
        queue.append(f"Analyse {ch}")

    print("\nQueue Processing:")
    while queue:
        task = queue.pop(0)
        print(f"Processing: {task}")


# Task 7: Number Pattern
def print_number_pattern(number):
    print("\nNumber Pattern:")
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# Task 8: Recursive Digit Sum
def recursive_digit_sum(student_id):
    if student_id == 0:
        return 0
    return student_id % 10 + recursive_digit_sum(student_id // 10)


# Display Summary
def display_summary(code, freq, vowels, consonants, is_balanced, digit_sum):
    print("\n===== Results =====")
    print(f"Personal Code: {code}")

    print("\nCharacter Frequency:")
    for k, v in freq.items():
        print(f"{k} : {v}")

    print("\nUnique Vowels:", ", ".join(sorted(vowels)))
    print("Unique Consonants:", ", ".join(sorted(consonants)))

    print("\nBalanced Brackets:", "Yes" if is_balanced else "No")

    print(f"\nRecursive Digit Sum of Student ID: {digit_sum}")


# Main Program
def main():
    print("===== Personal Pattern Toolkit =====")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Full Name: ")
    keyword = input("Enter Keyword: ")
    number = get_valid_number()
    brackets = input("Enter bracket expression: ")

    code = generate_personal_code(student_id, keyword)
    freq = count_character_frequency(name)
    vowels, consonants = find_unique_vowels_consonants(name + keyword)
    is_balanced = check_balanced_brackets(brackets)

    display_summary(code, freq, vowels, consonants, is_balanced,
                    recursive_digit_sum(student_id))

    process_keyword_queue(keyword)
    print_number_pattern(number)


# Run program
if __name__ == "__main__":
    main()