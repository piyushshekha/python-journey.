nums = [12,7,5,20,8,3]   
def sum_evens(nums):   
    total = 0
    for num in nums: 
        if num % 2 == 0:
            total += num            
    return total
   
result = sum_evens(nums)
print(result)