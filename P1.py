def print_without_vowels(s):
    line=""
    vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in s:
        if i not in vowels:
            line+=i

    print(line)
