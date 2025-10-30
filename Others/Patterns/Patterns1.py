def Pattern1(n):
    for i in range(n):
        print('*')

def Patern2(n):
    for i in range(n):
        print('*' * i)
        
def Pattern3(n):
    for i in range(n):
        print('*' * (i + 1))

def Pattern4(n):
    for i in range(n):
        print('*' * (n - i))
        
def Pattern5(n):
    for i in range(n):
        print(' ' * i + '*' * (n - i))
def Pattern6(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))
        

n = int(input("Enter the number of rows: "))

print("Pattern 1:")
Pattern1(n)

print("Pattern 2:")
Patern2(n)

print("Pattern 3:")
Pattern3(n)

print("Pattern 4:")
Pattern4(n)

print("Pattern 5:")
Pattern5(n)

print("Pattern 6:")
Pattern6(n)
