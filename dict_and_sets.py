student = {
    "name" : "piyush",
    "city" : "jamnagar",
    "marks": 85,
}
print("dictionary")
print("student city :",student.get("city"))
print("return value",student.get("grade"))

student.update({"status":"pass"})

print("updated dictionary : ",student)

subject ={"python","java","c++","python","javascript","java","python"}

print("unique subject",subject)
print("total needed class",len(subject))
