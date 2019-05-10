def buildMinHeap(v, n):
    global swaps
    for i in range(n): 
        if v[i] < v[int((i - 1) / 2)]: 
            j = i  
 
            while v[j] < v[int((j - 1) / 2)]:
                k = int((j - 1) / 2)
                (v[j], v[k]) = (v[k], v[j])
                swaps += 1 
                j = k
                if j == 0:
                    break


def heap_sort_interativo(v):  
    global swaps
    swaps = 0
    n = len(v)
    buildMinHeap(v, n)  
  
    for i in range(n - 1, 0, -1): 
        v[0], v[i] = v[i], v[0] 
        swaps += 1
        j, index = 0, 0
          
        while True: 
            index = 2 * j + 1

            if (index < (i - 1) and v[index] > v[index + 1]):  
                index += 1
 
            if index < i and v[j] > v[index]: 
                v[j], v[index] = v[index], v[j]
                swaps += 1  
          
            j = index  
            if index >= i: 
                break
    
    return swaps