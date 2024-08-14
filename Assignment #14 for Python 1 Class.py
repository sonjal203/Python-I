def power(b,n):
    result = 1
    for _ in range(n):
       result *= b
    return result

#Test the function with b = 2 and n = 5
b = 2
n = 5
result = power(b,n)
print(f"{b}^{n} = {result}")