from math import floor

# Basically used the sudo code from the book with a python twist
# A is list, p is first index, q is middle, r is last index
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = list()
    R = list()
    for i in range(1,n1+1):
        L.append(A[p+i-1])
    for j in range(1,n2+1):
        R.append(A[q+j])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

# Here A is the list, p is the firt index, and r is the last index
def mergesort(A,p,r):
    if p < r:
        q = floor((p+r)/2)
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)