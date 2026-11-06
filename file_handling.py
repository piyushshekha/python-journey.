with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing python.\n")
    
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    word = "learning"
    if word in data:
        print("found learning")
    else:
        print("not found")
        
        