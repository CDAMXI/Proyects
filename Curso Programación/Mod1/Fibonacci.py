def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
num = int(input("Ingrese un número: "))
print(f"El número Fibonacci de {num} es: {fibonacci(num)}")
#El 0 está en la posición 0, el 1 en la posición 1, etc.
