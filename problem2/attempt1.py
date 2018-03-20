fib = [1,2]

def next_fib():
    fib_length = len(fib)
    return fib[fib_length - 1] + fib[fib_length - 2]

def build_fib(max):
    while True:
        next_item = next_fib()
        if next_item <= max:
            fib.append(next_item)
        else:
            break

def compute_even_sum():
    build_fib(4000000)
    sum = 0
    for fib_num in fib:
        if(fib_num % 2) == 0:
            sum += fib_num           
    return sum    
