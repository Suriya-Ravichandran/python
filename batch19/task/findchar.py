from collections import Counter

data = "racecar"
char_count = Counter(data)

print(char_count)

# Print only characters that are repeated
for char, count in char_count.items():
    if count > 1:
        print(f"{char} = {count}")
