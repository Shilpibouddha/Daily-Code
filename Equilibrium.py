
#Q.3 Equilibrium index of an array

def findEquilibrium(a,n):
    total_sum = sum(a)
    left_sum = 0
    for i in range(len(a)):
        total_sum -= a[i]
        if left_sum == total_sum:
            return i
        left_sum += a[i]
    return -1
