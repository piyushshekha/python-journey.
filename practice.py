def print_list(list,index=0):
    if (index == len(list)):
        return
    print(list[index])
    print(list,index+1)
    
bike = ["honda","re","kn","ns"]
print_list(bike)
    