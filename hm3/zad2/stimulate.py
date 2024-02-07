import random
def stimulate(n):
    arr = [ random.randint(1, n) for i in range(n)]
    comparisons, swaps = 0, 0

    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        while j >= 0:
            comparisons += 1    
            if key < arr[j]:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    
    return comparisons, swaps