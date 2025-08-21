import hashlib
import itertools
import string

def md5_crack(target_hash, max_length=5):
    characters = string.ascii_lowercase  # You can also add digits or more symbols

    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            word = ''.join(attempt)
            if hashlib.md5(word.encode()).hexdigest() == target_hash:
                return word
    return None

# Example
hash_to_crack = 'fc5e038d38a57032085441e7fe7010b0'  # md5('hello')
original = md5_crack(hash_to_crack, max_length=5)

print(f'Original word: {original}' if original else 'No match found.')
