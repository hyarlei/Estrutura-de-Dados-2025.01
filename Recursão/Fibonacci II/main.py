memo_f = {}
memo_b = {}

def b(month_idx):
    
    if month_idx in memo_b:
        return memo_b[month_idx]
    
    if month_idx <= 0:
        result = 0
    elif month_idx == 1:
        result = 1
    elif month_idx == 2:
        result = 0
    else:

        result = b(month_idx - 2) + b(month_idx - 3)
    
    memo_b[month_idx] = result
    return result

def f(n_months):
    
    if n_months in memo_f:
        return memo_f[n_months]

    if n_months <= 0:
        result = 0
    elif n_months == 1:
        result = 1
    elif n_months == 2:
        result = 1
    else:
        result = f(n_months - 1) + b(n_months - 2)
        
    memo_f[n_months] = result
    return result

n = int(input())

print(f(n))