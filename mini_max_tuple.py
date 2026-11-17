def find_extremes(num):
    num.sort()
    return (num[0],num[-1])


result = find_extremes([45, 12, 89, 72, 34])

print("min to max :",result)
