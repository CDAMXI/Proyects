def Pattern1(n):
    # Constant single column
    for i in range(n):
        print('*')

def Pattern2(n):
    # Constant right-aligned single column
    for i in range(n):
        print(' ' * (n - 1) + '*')

def Pattern3(n):
    # Left-aligned increasing triangle
    for i in range(n):
        print('*' * (i + 1))

def Pattern4(n):
    # Left-aligned decreasing triangle
    for i in range(n):
        print('*' * (n - i))

def Pattern5(n):
    # Right-aligned increasing triangle
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))

def Pattern6(n):
    # Right-aligned decreasing triangle
    for i in range(n):
        print(' ' * i + '*' * (n - i))

def Pattern7(n):
    # Centered pyramid
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

def Pattern8(n):
    # Inverted centered pyramid
    for i in range(n):
        print(' ' * i + '*' * (2 * (n - i) - 1))

def Pattern9(n):
    # Diamond (combines Pattern7 + Pattern8)
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))


# Main execution
n = int(input("Enter the number of rows: "))

print("Pattern 1:")
Pattern1(n)
print()

print("Pattern 2:")
Pattern2(n)
print()

print("Pattern 3:")
Pattern3(n)
print()

print("Pattern 4:")
Pattern4(n)
print()

print("Pattern 5:")
Pattern5(n)
print()

print("Pattern 6:")
Pattern6(n)
print()

print("Pattern 7:")
Pattern7(n)
print()

print("Pattern 8:")
Pattern8(n)
print()

print("Pattern 9:")
Pattern9(n)
