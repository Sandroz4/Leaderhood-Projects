def backwards_prime(start, stop):
    def is_prime(x):
        if x <= 1:
            return False
        if x == 2:
            return True
        if x%2 == 0:
            return False
        for i in range(3, int(x**0.5)+1, 2):
            if x%i == 0:
                return False
        return True
    
    res = []
    for i in range(start, stop +1):
        if is_prime(i):
            reversed = int(str(i)[::-1])
            if is_prime(reversed) and i != reversed:
                res.append(i)
    return res
            
    
backwards_prime(2, 100)