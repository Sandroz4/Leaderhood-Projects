def solution(array_a, array_b):
    res = 0 
    output = 0 
    
    while res < len(array_a):
        mean = abs(array_a[res] - array_b[res])
        output += mean**2
        res +=1
        
    return output / len(array_a)