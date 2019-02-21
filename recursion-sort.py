def sortA(A):
    if len(A)==1:
        return True
    return A[0]<=A[1] and sortA(A[1:])
A=[1,2,3,4,5]
print(sortA(A))
