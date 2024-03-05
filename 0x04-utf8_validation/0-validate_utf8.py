#!/usr/bin/python3


def validUTF8(data):
    # Counter to keep track of the number of bytes left in a multi-byte character
    bytes_left = 0

    for byte in data:
        # Consider only the 8 least significant bits of each integer
        byte = byte & 0xFF

        # Check if the current byte is a continuation byte
        if bytes_left > 0:
            if (byte >> 6) == 0b10:
                bytes_left -= 1
            else:
                return False
        else:
            # Determine the number of bytes for the current character
            if byte >> 7 == 0:
                bytes_left = 0  # 1-byte character
            elif byte >> 5 == 0b110:
                bytes_left = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                bytes_left = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                bytes_left = 3  # 4-byte character
            else:
                return False  # Invalid leading bits for UTF-8 character

    # Check if there are any remaining bytes left
    return bytes_left == 0
