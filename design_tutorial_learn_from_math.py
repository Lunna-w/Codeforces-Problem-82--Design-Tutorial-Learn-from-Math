def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

x = 4  
y = n - x

while is_prime(x) or is_prime(y):
    x += 1
    y = n - x

print(x, y)