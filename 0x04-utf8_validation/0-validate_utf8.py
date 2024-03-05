#!/usr/bin/python3

def validUTF8(data):
    # Helper function to check if a byte is a valid UTF-8 continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        leading_bits = data[i] >> 5

        if leading_bits == 0b11110:  # 4-byte character
            if i + 3 >= len(data) or any(not is_continuation(data[j]) for j in range(i + 1, i + 4)):
                return False
            i += 4
        elif leading_bits == 0b1110:  # 3-byte character
            if i + 2 >= len(data) or any(not is_continuation(data[j]) for j in range(i + 1, i + 3)):
                return False
            i += 3
        elif leading_bits == 0b110:  # 2-byte character
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif leading_bits == 0:  # 1-byte character
            i += 1
        else:
            return False  # Invalid leading bits for UTF-8 character

    return True
