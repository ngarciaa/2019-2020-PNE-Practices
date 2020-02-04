#-- 1 + 2 +3 + .... + 20
#-- 1 + ....... + 100

def sumn (n) :
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum

print ('sum of 1-20:', sumn(20))
print ('sum of 1-100:', sumn(100))