import base64

# Base64 encoding function
def encode_base64(input_string):
    try:
        # Convert the input string to bytes
        input_bytes = input_string.encode('utf-8')
        # Encode the bytes into Base64
        encoded_bytes = base64.b64encode(input_bytes)
        # Convert Base64 bytes back to a string
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string
    except Exception as e:
        return f"Error encoding to Base64: {e}"

# Example usage
input_string = "SuriyaRavichandran"# Example string
input_string=input_string[3:7]
print(input_string)
encoded_string = encode_base64(input_string)
print("Encoded String:", encoded_string)
# Base64 decoding function
def reverse_base64(encoded_string):
    try:
        # Decode the Base64 string
        decoded_bytes = base64.b64decode(encoded_string)
        # Convert bytes to string
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"Error decoding Base64: {e}"

# Example usage
encoded_string = encoded_string  # Example Base64 string
decoded_string = reverse_base64(encoded_string)
print("Decoded String:", decoded_string)






