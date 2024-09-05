#!/usr/bin/python3
"""
0-UTF-8 Validation
"""


def validUTF8(data):
    # Number of bytes to process in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Extract the least significant 8 bits (since data may have larger integers)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check how many leading 1's are there in the first byte
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0
                return False
        else:
            # Check if the byte is a continuation byte (must start with 10)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are leftover bytes expected, return False
    return num_bytes == 0
