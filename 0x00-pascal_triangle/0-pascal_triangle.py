#!/usr/bin/python3

def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            previous_row = triangle[i-1]

            for j in range(1, i):
                value = previous_row[j-1] + previous_row[j]
                row.append(value)

            row.append(1)

        triangle.append(row)

    return triangle
