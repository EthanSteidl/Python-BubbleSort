def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(0, len(a)-1-i):
            if(a[j+1] < a[j]):
                a[j], a[j+1] = a[j+1],a[j]