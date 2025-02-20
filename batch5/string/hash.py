import hashlib
import os

# Function to generate a salt
def generate_salt():
    return os.urandom(16)  # 16 bytes (128 bits) of random data

# Function to create a hash using SHA-256
def create_hash(input_data, salt):
    # Combine the input data and salt
    salted_input = salt + input_data.encode('utf-8')
    # Create a SHA-256 hash
    hash_object = hashlib.sha256(salted_input)
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Function to verify a hash
def verify_hash(input_data, salt, original_hash):
    # Recreate the hash using the same salt and input data
    new_hash = create_hash(input_data, salt)
    # Compare the new hash with the original hash
    return new_hash == original_hash

# Example usage
if __name__ == "__main__":
    # Input data (e.g., a password)
    password = "my_secure_password"

    # Step 1: Generate a salt
    salt = generate_salt()
    print(f"Salt: {salt.hex()}")

    # Step 2: Create a hash
    hashed_password = create_hash(password, salt)
    print(f"Hashed Password: {hashed_password}")

    # Step 3: Verify the hash
    is_valid = verify_hash(password, salt, hashed_password)
    print(f"Hash Verification: {'Success' if is_valid else 'Failed'}")