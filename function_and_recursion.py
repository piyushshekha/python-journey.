def calc_avg(a,b,c):
    total = a + b + c
    avg = total /3
    return avg
      
result = calc_avg(19,3,5)
print("average is :",result)

def factorial(n):
    if(n == 0 or n== 1):
        return 1
    else:
        return n * factorial(n-1)
    
print("the factorial is :",factorial(5))    