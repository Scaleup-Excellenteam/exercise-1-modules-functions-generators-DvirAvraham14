import re

secret_messages = []
with open('resources/logo.jpg', 'rb') as f:
    # Read the file in chunks of 1024 bytes at a time
    bits_size = 1024
    while True:
        data = f.read(bits_size)
        if not data:
            break
        # Search for strings ending in "!" using regular expressions
        matches = re.findall(b'[a-z]{5,}!', data)
        for match in matches:
            # Decode the binary string to a Unicode string and append to the list of secret messages
            secret_messages.append(match.decode())

print(secret_messages)
