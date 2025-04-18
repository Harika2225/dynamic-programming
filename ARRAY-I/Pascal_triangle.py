import math

def get_element_at(r, c):
    if c > r or c <= 0 or r <= 0:
        return 0 
    return math.comb(r - 1, c - 1)  
print(get_element_at(5, 3))  


def get_nth_row(n):
    row = []
    for c in range(n):
        row.append(math.comb(n - 1, c))
    return row
print(get_nth_row(5)) 


def generate_pascals_triangle(n):
    triangle = []
    for r in range(1, n + 1):
        row = []
        for c in range(r):
            row.append(math.comb(r - 1, c))
        triangle.append(row)
    return triangle
rows = generate_pascals_triangle(5)
for row in rows:
    print(row)
