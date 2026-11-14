# 1. Slicing (Stop 5 exclude hoga):
s = "PYTHON"
print("Slicing [1:5:2] :", s[1:5:2])

# 2. Aliasing (Dono ek hi memory box hain):
a = [10, 20]
b = a
b.append(30)
print("Length of a     :", len(a))

# 3. Dict get (None dega, crash nahi karega):
data = {"id": 101}
print("get('salary')   :", data.get("salary"))