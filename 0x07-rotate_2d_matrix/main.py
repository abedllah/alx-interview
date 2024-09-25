#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[9,12, 3],
              [4, 55, 6],
              [7, 8, 6]]

    rotate_2d_matrix(matrix)
    print(matrix)
