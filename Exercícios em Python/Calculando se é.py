n = int(input())
eh_primo = 1

if n < 2:
    eh_primo = 0
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = 0
            break
        
print(eh_primo)